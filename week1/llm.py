import json
from google import genai
from dotenv import load_dotenv
from structured import schema, Contact

load_dotenv()

client = genai.Client()

# Week 1 - Task 1 : Call the model and analyse tokens
# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Say hi in one sentence."
# )

# Week 1 - Task 1 : Analyse how response varies with temperature
# BASIC 
# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents = "Invent a name for a coffee shop. Just need one name",
#     config={
#         "temperature": 0.0
#     }
# )
# BOTH 
# for temperature in [0.0, 1.0]:
#     print(f"\n--- Temperature {temperature} ---")

#     for _ in range(3):
#         response = client.models.generate_content(
#             model="gemini-3.6-flash",
#             contents = "Invent a name for a coffee shop. Just need one name",
#             config={"temperature": temperature}
#         )

#         print(response.text.strip())

# print("Response:", response.text)
# usage = response.usage_metadata
# print("Input tokens:", usage.prompt_token_count)
# print("Output tokens:", usage.candidates_token_count)
# print("Thinking tokens:", usage.thoughts_token_count)
# print("Total tokens:", usage.total_token_count)

# WEEK 1 - TASK 2 : Extract and validate json data from text

# CASE 1 : Correct data 
blob = "hey it's Walter White, ping me at heisenberg@bluepill.co"

prompt = f"""
Extract a Contact as JSON matching this schema: {schema}
Text: {blob}
Return ONLY the JSON object.
"""

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents=prompt,
# )

# print(f" Model response : {response.text}")
# Case 1 : Correct data
# data = json.loads(response.text)
# Case 2 : Corrupted data - Validation Error
data = {
    "name": 123,
    "email": "dana@acme.co",
    "company": "Acme",
    "country" : "Australia"
}

# WEEK 1 - TASK 2B : corrupted ```json response....
# response = '''```json
# {"name": "Dana", "email": "dana@acme.co", "company": "Acme"}
# ```'''
# cleaned = response.replace("```json", "").replace("```", "").strip()
# data = json.loads(cleaned)

# print(f"Converted to python dictionary : {data}")
# print(f"Dict type : {type(data)}")

contact = Contact.model_validate(data)
print(f"Object validation reponse : {contact}")


