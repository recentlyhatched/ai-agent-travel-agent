import requests

def get_weather(city: str) -> str:
    """
    Uses Open-Meteo (free, no API key) with minimal logic.
    """

    # very small built-in city mapping (only for demo stability)
    city = city.lower().strip()

    locations = {
        "london": (51.5072, -0.1276),
        "paris": (48.8566, 2.3522),
        "new york": (40.7128, -74.0060),
    }

    if city not in locations:
        return "City not supported. Try: London, Paris, New York"

    lat, lon = locations[city]

    # call weather API
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    data = requests.get(url).json()

    weather = data["current_weather"]

    return f"""
    {city.title()}
    Temp: {weather['temperature']}°C
    Wind: {weather['windspeed']} km/h
"""