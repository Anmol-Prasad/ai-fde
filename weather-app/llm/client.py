from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather information for a city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The name of the city."
            }
        },
        "required": ["city"]
    }
}

stock_tool = {
    "name": "get_stock_price",
    "description": "Get the current stock price for a company.",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The stock ticker symbol, such as AAPL or NVDA."
            }
        },
        "required": ["symbol"]
    }
}

calculator_tool = {
    "name": "calculate",
    "description": "Perform a mathematical calculation.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {
                "type": "number"
            },
            "b": {
                "type": "number"
            },
            "operation": {
                "type": "string",
                "enum": [
                    "add",
                    "subtract",
                    "multiply",
                    "divide"
                ]
            }
        },
        "required": [
            "a",
            "b",
            "operation"
        ]
    }
}

def ask_llm(user_input: str):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input,
        config={
            "tools": [
                {
                    "function_declarations": [weather_tool, stock_tool]
                }
            ],
            "tool_config": {
                "function_calling_config": {
                    "mode": "ANY"
                }
            }
        }
    )

    return response