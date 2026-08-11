from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: str


class CalculatorResponse(BaseModel):
    result: float