from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

inputs = [
    "Mike from Globex, mike@globex.com",
    "Sarah - BetaCorp - sarah@beta.com",
    "John works at Acme Labs, john@acme.io",
    "Lisa, Foo Inc, lisa@foo.com",
    "Tom from Startup, tom@startup.io"
]

naive = "Extract the contact info: {x}"

structured = (
    "Extract name, email, company as JSON.\n"
    "Example: 'Sam at Foo, sam@foo.io' -> "
    '{{"name":"Sam","email":"sam@foo.io","company":"Foo"}}\n'
    "Example: 'Dana at Acme, dana@acme.co' -> "
    '{{"name":"Dana","email":"dana@acme.co","company":"Acme"}}\n'
    "Now: {x}\n"
    "Return ONLY JSON."
)

for x in inputs:
    for label, prompt in [("naive", naive), ("structured", structured)]:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt.format(x=x)
        )

        print(label, "->", response.text.strip())