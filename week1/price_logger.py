from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


# $ per token
PRICE = {
    "in": 3 / 1_000_000,
    "out": 15 / 1_000_000
}


def log_cost(usage):
    input_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count

    cost = (
        input_tokens * PRICE["in"]
        + output_tokens * PRICE["out"]
    )

    print(f"Input tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Estimated cost: ${cost:.6f}")


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what an API is in one sentence."
)

log_cost(response.usage_metadata)