from schemas.weather import WeatherRequest, WeatherResponse


def get_weather(request: WeatherRequest) -> WeatherResponse:

    fake_data = {
        "Pune": {
            "temperature": 29,
            "humidity": 72,
            "condition": "Cloudy"
        },
        "Delhi": {
            "temperature": 35,
            "humidity": 55,
            "condition": "Sunny"
        },
        "Mumbai": {
            "temperature": 30,
            "humidity": 80,
            "condition": "Rainy"
        }
    }

    data = fake_data.get(request.city)

    if data is None:
        raise ValueError(
            f"Weather data not available for {request.city}"
        )

    return WeatherResponse(
        city=request.city,
        **data
    )


if __name__ == "__main__":
    request = WeatherRequest(city="Pune")

    response = get_weather(request)

    print(response)