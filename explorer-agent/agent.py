import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def search_datasets(query: str) -> list:
    """Retrieves geospatial data sets"""
    coordinates = [
        [40.7128, -74.0060],
        [51.5072, -0.1276],
        [35.6895, 139.6917],
    ]
    return coordinates

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-pro-preview-06-05",
    description=(
        "Agent to search and return coordinates for datasets."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about geospatial datasets"
    ),
    tools=[search_datasets],
)
