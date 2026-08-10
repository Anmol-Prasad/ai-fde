# WEEK 1 - Task 3 : Make the LLM call an external tool and add that response in the LLM response
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

client = genai.Client()

def calculator(expr : str):
    return eval(expr)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is 23 * 19?",
    config={
        "tools": [calculator],
         "automatic_function_calling": {
            "disable": True
        }
    }
)

part = response.candidates[0].content.parts[0]

print("Function name:", part.function_call.name)
print("Arguments:", part.function_call.args)

function_call = part.function_call
result = calculator(function_call.args["expr"])
print("Tool result:", result)

function_response_part = types.Part.from_function_response(
    name=function_call.name,
    response={"result": result}
)

contents = [
    "What is 23 * 19?",
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[function_response_part]
    )
]

final_response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config={
        "tools": [calculator],
        "automatic_function_calling": {
            "disable": True
        }
    }
)

print("Final answer:", final_response.text)