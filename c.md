This is a known issue with the way window sizing is handled in browser-use v0.1.45. The problem occurs specifically when setting the window size with BrowserContextConfig while also using `no_viewport=True`.

## Solution:

1. Remove the `no_viewport=True` parameter, as it overrides your window size settings:

```python
browser_context_config = BrowserContextConfig(
    window_width=800,
    window_height=600,
    wait_for_network_idle_page_load_time=5.0,
    locale='en-US',
    highlight_elements=True,
    viewport_expansion=500,
)
```

2. Alternatively, configure the browser directly using BrowserConfig:

```python
from browser_use import BrowserConfig

browser_config = BrowserConfig(
    headless=False,
    # Other browser settings
)

browser = Browser(config=browser_config)

# Then create your context with the desired dimensions
browser_context_config = BrowserContextConfig(
    window_width=800,
    window_height=600,
    # Other context settings
)
browser_context = BrowserContext(browser=browser, config=browser_context_config)
```

3. For a simplified approach, pass the configuration directly to the Agent:

```python
from browser_use import Agent, BrowserContextConfig
from langchain_google_genai import ChatGoogleGenerativeAI

browser_context_config = BrowserContextConfig(
    window_width=800,
    window_height=600,
    wait_for_network_idle_page_load_time=5.0,
)

agent = Agent(
    task=prompt,
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro-preview-05-06"),
    browser_context_config=browser_context_config,  # Pass config directly here
    use_vision=True,
    use_vision_for_planner=True,
)

await agent.run()
```

The issue occurs because when `no_viewport=True` is set, it tells the browser to ignore viewport settings, which includes the window dimensions. The library is designed to prioritize this flag over the dimension settings for compatibility with certain websites.

This will be fixed in the next release to ensure window dimensions are respected regardless of the viewport setting. 