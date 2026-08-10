import json
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

# Extending BaseModel means that class is a pydantic model 
class Contact(BaseModel):
    name: str
    email: str | None = None
    company: str | None = None

contact = Contact(
    name="Don Critioli",
    email="doncristioli@acme.co",
    company="Acme"
)

schema = Contact.model_json_schema()

load_dotenv()
client = genai.Client()

def extract_contact(text):
    prompt = f"""
    Extract a Contact as JSON matching this schema:
    {schema}
    Text: {text}
    Return ONLY the JSON object.
    """
    
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    data = json.loads(response.text)

    return Contact.model_validate(data)
