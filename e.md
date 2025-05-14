 Multiple User session #1622

@rh-id Yes, browser-use can maintain login sessions and supports manual login + agent takeover. Examples:

## 1. Cookies File Method

```python
# From browser_use/browser/context.py line 1798:
async def save_cookies(self):
    """Save current cookies to file"""
    if self.session and self.session.context and self.config.cookies_file:
        try:
            cookies = await self.session.context.cookies()
            logger.debug(f'🍪  Saving {len(cookies)} cookies to {self.config.cookies_file}')

            # Check if the path is a directory and create it if necessary
            dirname = os.path.dirname(self.config.cookies_file)
            if dirname:
                os.makedirs(dirname, exist_ok=True)

            async with await anyio.open_file(self.config.cookies_file, 'w') as f:
                await f.write(json.dumps(cookies))
```

Implementation:
```python
#psuedocode
from browser_use import Agent, Browser, BrowserContext, BrowserContextConfig

browser = Browser()
context = BrowserContext(
    browser=browser, 
    config=BrowserContextConfig(cookies_file="gmail_cookies.json")
)
agent = Agent(task="Summarize emails", browser_context=context, llm=llm)
```

## 2. Connect to Your Real Browser

```python
# From browser_use/browser/browser.py line 188:
async def _setup_user_provided_browser(self, playwright: Playwright) -> PlaywrightBrowser:
	"""Sets up and returns a Playwright Browser instance with anti-detection measures."""
	if not self.config.browser_binary_path:
			raise ValueError('A browser_binary_path is required')

    assert self.config.browser_class == 'chromium', (
        'browser_binary_path only supports chromium browsers (make sure browser_class=chromium)'
    )

    try:
        # Check if browser is already running
```

Usage:
```python
browser = Browser(
    config=BrowserConfig(
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    )
)
agent = Agent(task="Summarize emails", browser=browser, llm=llm)
```

Each BrowserContext is isolated but shares the same browser process. 