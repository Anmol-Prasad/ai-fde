from fastapi import FastAPI

from core.orchestrator import run
from schemas.api import Query, Answer



app = FastAPI()


@app.post("/invoke", response_model=Answer)
def invoke(q: Query):

    response = run(q.question)

    output = response.text

    usage = response.usage_metadata

    tokens = (
        getattr(usage, "prompt_token_count", 0)
        + getattr(usage, "candidates_token_count", 0)
    )

    return Answer(
        output=output,
        citations=[],
        metadata={
            "tokens": tokens,
            "cost_usd": 0.0
        }
    )