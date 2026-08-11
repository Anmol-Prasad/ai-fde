from schemas.calculator import (
    CalculatorRequest,
    CalculatorResponse,
)


def calculate(request: CalculatorRequest) -> CalculatorResponse:

    if request.operation == "add":
        result = request.a + request.b

    elif request.operation == "subtract":
        result = request.a - request.b

    elif request.operation == "multiply":
        result = request.a * request.b

    elif request.operation == "divide":
        if request.b == 0:
            raise ValueError("Cannot divide by zero")

        result = request.a / request.b

    else:
        raise ValueError(
            f"Unknown operation: {request.operation}"
        )

    return CalculatorResponse(result=result)