import asyncio
from dotenv import load_dotenv
from browser_use import Agent, Browser
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from langchain_openai import ChatOpenAI
#for your model
load_dotenv()

async def setup_browser():
    # Create browser without arguments
    browser = Browser()
    return browser

async def setup_browser_context(browser: Browser):
    config = BrowserContextConfig(
        window_height=500,
        window_width=1440,
        no_viewport=False,  # This is important for respecting dimensions
    )
    return BrowserContext(browser=browser, config=config)

async def main():
    # Initialize components
    browser = await setup_browser()
    browser_context = await setup_browser_context(browser)
    
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        # Create agent with browser context
        agent = Agent(
            task="find the weather in New York",
            browser_context=browser_context,
            llm=llm,
        )
        # Run agent
        await agent.run(max_steps=10)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # CRITICAL: Close the browser_context and browser directly
        # Don't try to access agent.browser as it doesn't exist
        await browser_context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 