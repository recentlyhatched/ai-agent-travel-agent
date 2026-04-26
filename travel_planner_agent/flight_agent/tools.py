from urllib.parse import quote_plus

def search_flights_simple(origin: str, destination: str, date: str) -> dict:
    """Returns a Google Flights search link."""
    query = f"Flights from {origin} to {destination} on {date}"
    url = f"https://www.google.com/travel/flights?q={quote_plus(query)}"
    return {
        "status": "success",
        "message": "Here are available flight options.",
        "origin": origin,
        "destination": destination,
        "date": date,
        "booking_url": url,
    }