# Setting up a Tor Proxy with Browser Use

To configure Browser Use to work with your Tor proxy, you need to use the `proxy` parameter in the `BrowserConfig` class. Here's how to do it:

## How to Configure the Tor Proxy

Browser Use's proxy configuration is based on Playwright's proxy settings. Looking at [`browser_use/browser/browser.py:36-57`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L36-L57), we can see the `ProxySettings` class:

```python
class ProxySettings(BaseModel):
    """the same as playwright.sync_api.ProxySettings, but now as a Pydantic BaseModel so pydantic can validate it"""

    server: str
    bypass: str | None = None
    username: str | None = None
    password: str | None = None

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    # Support dict-like behavior for compatibility with Playwright's ProxySettings
    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default=None):
        return getattr(self, key, default)
```

Then, in [`browser_use/browser/browser.py:345-352`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L345-L352), we can see how the proxy configuration is actually used:

```python
browser = await browser_class.launch(
    channel='chromium',  # https://github.com/microsoft/playwright/issues/33566
    headless=self.config.headless,
    args=args[self.config.browser_class],
    proxy=self.config.proxy.model_dump() if self.config.proxy else None,
    handle_sigterm=False,
    handle_sigint=False,
)
```

## Example Code

For a Tor proxy (which typically runs on `localhost:9050` as a SOCKS5 proxy), here's how you would configure it:

```python
from browser_use import Browser, BrowserConfig, ProxySettings
proxy_settings = ProxySettings(
    server="socks5://127.0.0.1:9050"
)

# Create browser config with proxy settings
browser_config = BrowserConfig(
    proxy=proxy_settings
)

browser = Browser(config=browser_config)
```

## Using from CLI

If you're using the CLI tool, you can modify your config to include proxy settings:

```python
# In your browser-use config
config = {
    "browser": {
        "proxy": {
            "server": "socks5://127.0.0.1:9050"
        }
    }
}
```

## Additional Notes

1. Make sure your Tor service is running before starting Browser Use
2. The standard Tor SOCKS5 proxy runs on `127.0.0.1:9050` by default
3. If your Tor proxy requires authentication, you can add the `username` and `password` fields to the `ProxySettings` object
4. For some websites, you may need to set `"ignore_https_errors": true` in your browser context config to handle SSL issues with Tor

For more details on Playwright's proxy configuration format, refer to the [Playwright documentation](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-proxy). 