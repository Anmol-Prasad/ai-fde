from google.genai import types

from llm.client import (
    client,
    weather_tool,
    stock_tool,
    calculator_tool,
)

from schemas.calculator import CalculatorRequest
from tools.calculator import calculate
from schemas.weather import WeatherRequest
from schemas.stocks import StockRequest

from tools.weather import get_weather
from tools.stocks import get_stock_price


TOOL_CONFIG = {
    "get_weather": {
        "function": get_weather,
        "schema": WeatherRequest,
    },

    "get_stock_price": {
        "function": get_stock_price,
        "schema": StockRequest,
    },

    "calculate": {
        "function": calculate,
        "schema": CalculatorRequest,
    },
}


TOOLS = [
    weather_tool,
    stock_tool,
    calculator_tool,
]


def run(user_input: str) -> str:

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input,
        config={
            "tools": [
                {
                    "function_declarations": TOOLS
                }
            ],
            "tool_config": {
                "function_calling_config": {
                    "mode": "ANY"
                }
            }
        }
    )

    for candidate in response.candidates:
        for part in candidate.content.parts:

            if not part.function_call:
                continue

            function_call = part.function_call

            tool_name = function_call.name
            tool_args = function_call.args

            print("Tool requested:", tool_name)
            print("Raw arguments:", tool_args)

            # Find tool configuration
            config = TOOL_CONFIG.get(tool_name)

            if config is None:
                raise ValueError(
                    f"Unknown tool: {tool_name}"
                )

            # Validate arguments using the correct schema
            request = config["schema"](**tool_args)

            print("Validated request:", request)

            # Execute tool
            result = config["function"](request)

            print("Tool result:", result)

            # Send result back to Gemini
            final_response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_text(
                                text=user_input
                            )
                        ]
                    ),
                    response.candidates[0].content,
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_function_response(
                                name=tool_name,
                                response=result.model_dump()
                            )
                        ]
                    )
                ],
                config={
                    "tools": [
                        types.Tool(
                            function_declarations=TOOLS
                        )
                    ]
                }
            )

            return final_response
            # return final_response.text 

    return response
    # return response.text 