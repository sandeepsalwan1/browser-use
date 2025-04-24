from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os

async def main():
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Please set your OPENAI_API_KEY environment variable")
        return
    
    agent = Agent(
        task="Search for 'browser-use github' and open the repository page",
        llm=ChatOpenAI(model="gpt-4o", api_key=api_key),
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main()) 