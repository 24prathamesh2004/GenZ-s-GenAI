from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import requests

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather data for a city"""
    url = f"https://api.weatherstack.com/current?access_key=YOUR_KEY&query={city}"
    return requests.get(url).json()

# NEW API
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
)

# invoke
response = agent.invoke({"messages": [{"role": "user", "content": "Who won yesterday's IPL match?"}]})

print(response)