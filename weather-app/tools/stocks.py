from schemas.stocks import StockRequest, StockResponse


def get_stock_price(request: StockRequest) -> StockResponse:

    fake_data = {
        "AAPL": {
            "price": 227.50,
            "currency": "USD"
        },
        "GOOGL": {
            "price": 201.30,
            "currency": "USD"
        },
        "NVDA": {
            "price": 181.20,
            "currency": "USD"
        }
    }

    data = fake_data.get(request.symbol.upper())

    if data is None:
        raise ValueError(
            f"Stock data not available for {request.symbol}"
        )

    return StockResponse(
        symbol=request.symbol.upper(),
        **data
    )