
from google.adk.agents.llm_agent import Agent
from flight_agent.tools import search_flights_simple

flight_agent = Agent(
    name="flight_agent",
    model="gemini-2.5-flash",
    description="Handles flight searches and returns Google Flights links.",
    tools=[search_flights_simple],
    instruction="""
You are a helpful flight booking assistant.

Your job is to help users find flights.

Rules:
- Use search_flights_simple when the user asks for flights.
- If origin, destination, or travel date is missing, ask one short follow-up question.
- Always include the booking link in your response.
- Keep the answer short and practical.
""",
)