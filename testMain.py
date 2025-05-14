import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, Browser
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from langchain_openai import ChatOpenAI

load_dotenv()

async def test_with_issue():
    """Test that reproduces the window size issue"""
    print("\n🔴 Running test WITH the issue (no_viewport=True)")
    
    prompt = 'find name of ceo of ford'  # smoke test prompt
    
    browser_context_config = BrowserContextConfig(
        no_viewport=True,  # This causes the issue
        window_width=800,  
        window_height=600,
        wait_for_network_idle_page_load_time=5.0,
        locale='en-US',
        highlight_elements=True,
        viewport_expansion=500,
    )
    
    browser = Browser()
    browser_context = BrowserContext(browser=browser, config=browser_context_config)
    
    try:
        model = ChatOpenAI(model="gpt-4o", temperature=0)
        
        agent = Agent(
            task=prompt,
            browser_context=browser_context,
            llm=model,
        )
        
        print("Browser should open at full screen despite window_width=800, window_height=600")
        await agent.run(max_steps=10)  # Limiting steps for quick testing
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Note: We close the browser_context and browser directly, not through agent
        await browser_context.close()
        await browser.close()

async def test_with_fix():
    """Test with the fix applied (no no_viewport parameter)"""
    print("\n🟢 Running test WITH the fix (no_viewport=False)")
    
    prompt = 'find name of ceo of ford'  # smoke test prompt
    
    browser_context_config = BrowserContextConfig(
        no_viewport=False,  # Explicitly set to False for clarity
        window_width=600,
        window_height=600,
        wait_for_network_idle_page_load_time=5.0,
        locale='en-US',
        highlight_elements=True,
        viewport_expansion=500,
    )
    
    browser = Browser()
    browser_context = BrowserContext(browser=browser, config=browser_context_config)
    
    try:
        model = ChatOpenAI(model="gpt-4o", temperature=0)
        
        agent = Agent(
            task=prompt,
            browser_context=browser_context,
            llm=model,
        )
        
        print("Browser should now open at 200x600 as specified")
        await agent.run(max_steps=10)  # Limiting steps for quick testing
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Note: We close the browser_context and browser directly, not through agent
        await browser_context.close()
        await browser.close()

async def main():
    print("Testing browser-use window sizing issue")
    print("======================================")
    
    print("\n=== FIRST TEST: with no_viewport=True (should ignore window dimensions) ===")
    # await test_with_issue()  
    
    print("\nWaiting 5 seconds before next test...")
    # await asyncio.sleep(5)
    
    print("\n=== SECOND TEST: with no_viewport=False (should respect window dimensions) ===")
    await test_with_fix()    
    
if __name__ == "__main__":
    asyncio.run(main())