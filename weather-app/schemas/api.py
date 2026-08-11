from pydantic import BaseModel, Field


class Query(BaseModel):
    question: str = Field(min_length=1)


class Answer(BaseModel):
    output: str
    citations: list[str] = []
    metadata: dict = {}