import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

# Load environment variables
load_dotenv()

# Check if OpenAI API key is set
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError('OPENAI_API_KEY is not set. Add it to your .env file.')

async def main():
    # Create a browser with allowed domains configuration
    browser_config = BrowserConfig(
        headless=False,
        allowed_domains=['x.com', 'twitter.com']
    )
    
    browser = Browser(config=browser_config)
    
    # Initialize the model
    llm = ChatOpenAI(
        model='gpt-4o',
        temperature=0.0,
    )
    
    # Create the agent first
    agent = Agent(
        task='Go to x.com, log in with your account (I will enter the credentials manually), then create a post with the text "I autoposted this with @browser_use" and send it.',
        llm=llm,
        browser=browser,
    )
    
    # Run the agent
    await agent.run()
    
    # Don't forget to close the browser
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 