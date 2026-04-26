from google.adk.agents import Agent

from travel_planner_agent.flight_agent.agent import flight_agent
from travel_planner_agent.hotel_agent.agent import hotel_agent
from travel_planner_agent.itinerary_agent.agent import itinerary_agent


root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    description="Main travel planning agent that coordinates flights, stays, and itineraries.",
    sub_agents=[flight_agent, hotel_agent, itinerary_agent],
    instruction="""
You are a helpful travel agent.

Your job is to help the user plan trips, find flights, Airbnb stays, and create itineraries.

Available specialists:
- flight_agent for flights
- stay_agent for Airbnb stays
- itinerary_agent for trip plans

Rules:
- Delegate to the correct specialist based on the user's request.
- If the user asks for a complete trip, help with flights, stay, and itinerary.
- If the user has not provided enough details, ask one short follow-up question.
- Keep answers simple and helpful.
- When finished, reply with "DONE".
""",
)