# Using Incognito Mode in Browser Use

The `--incognito` flag doesn't work with Browser Use's standard configuration because of how Chrome handles incognito mode. Looking at the codebase, I can see why your approach isn't working and how to solve it.

## Why Your Current Approach Doesn't Work

In [`browser_use/browser/browser.py:309-372`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L309-L372), we can see that Browser Use handles Chrome launching differently than direct Playwright usage. When using `browser_binary_path`, Browser Use connects to Chrome via CDP (Chrome DevTools Protocol) after launching Chrome, rather than using Playwright's persistent context approach.

The problem is that when Chrome is launched with `--incognito`, each incognito window runs in a separate process, and the CDP connection can only connect to the main browser process, not to the incognito window.

## Solution: Using Temporary Profiles Instead

Instead of using the `--incognito` flag, you can achieve the same effect by creating a temporary, clean user profile for each session. Browser Use already supports this pattern:

```python
import uuid
from browser_use import Browser, BrowserConfig, BrowserContextConfig, Agent
from langchain_openai import ChatOpenAI

# Create a unique temporary profile directory
temp_profile_dir = f"/tmp/browser_use_profile_{uuid.uuid4()}"

# Configure the browser with this temporary profile
config = BrowserConfig(
    headless=False,
    browser_binary_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    extra_browser_args=[
        f"--user-data-dir={temp_profile_dir}",
        "--no-first-run",
        "--no-default-browser-check"
    ]
)

# Create browser and agent
browser = Browser(config=config)
agent = Agent(
    task="Your task here",
    llm=ChatOpenAI(model="gpt-4o"),
    browser=browser
)

# Run the agent
await agent.run()

# Optionally clean up the temporary directory when done
import shutil
shutil.rmtree(temp_profile_dir, ignore_errors=True)
```

## Why This Works Better Than Incognito

Looking at [`browser_use/browser/browser.py:365-378`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L365-L378), Browser Use creates a CDP connection to the Chrome instance. Using a clean profile gives you the same benefits as incognito mode:

1. No existing cookies
2. No saved logins or autofill data
3. No browser extensions (which may be part of your company SSO)
4. Fresh session for each run

This approach works better with the Browser Use architecture because:

1. It's compatible with how Browser Use connects to Chrome via CDP
2. It persists for the duration of your automation run
3. It can be easily cleaned up afterward

## Additional Configuration

If you need to ensure no company policies or enterprise configurations are applied, you can add these flags:

```python
extra_browser_args=[
    f"--user-data-dir={temp_profile_dir}",
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-sync",
    "--disable-extensions",
    "--disable-background-networking",
    "--disable-web-security"
]
```

These flags disable various Chrome features that might be part of your company's browser hardening and SSO integration, giving you a clean environment to work with.

## Understanding Browser Use's Architecture

Looking at the source code, particularly in [`browser_use/browser/browser.py:290-396`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L290-L396), Browser Use launches Chrome with specific arguments and then connects to it. The incognito window operates differently and isn't directly accessible through this approach. 