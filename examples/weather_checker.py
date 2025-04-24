from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
import json

async def main():
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Please set your OPENAI_API_KEY environment variable")
        return
    
    # Cities to check weather for
    cities = ["New York", "London", "Tokyo", "Sydney", "San Francisco"]
    
    # Create a browser-use agent to check weather
    agent = Agent(
        task=f"Check the current weather for these cities: {', '.join(cities)}. Create a JSON file named 'weather_data.json' with the temperature in Celsius and general conditions for each city.",
        llm=ChatOpenAI(model="gpt-4o", api_key=api_key),
    )
    await agent.run()
    
    # Read and display the results if the file was created
    try:
        with open('weather_data.json', 'r') as f:
            weather_data = json.load(f)
            print("\nWeather Data Summary:")
            print(json.dumps(weather_data, indent=2))
    except FileNotFoundError:
        print("\nWeather data file was not created.")

if __name__ == "__main__":
    asyncio.run(main()) 