from pydantic import BaseModel


class StockRequest(BaseModel):
    symbol: str


class StockResponse(BaseModel):
    symbol: str
    price: float
    currency: str