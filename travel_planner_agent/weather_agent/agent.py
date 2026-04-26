from google.adk.agents.llm_agent import Agent
from weather_agent.tools import get_weather

weather_agent = Agent(
    model="gemini-2.5-flash",
    name="weather_agent",
    description="Simple weather assistant",
    instruction="""
You are a weather assistant.

Use get_weather tool for any weather question.
Keep answers short.
""",
    tools=[get_weather]
)