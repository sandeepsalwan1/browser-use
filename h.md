# Solving "Failed to create new browser session" Error on Windows

When encountering the error `exception=NotImplementedError()` on Windows (while it works fine on Linux), the issue is likely related to the screen resolution detection in Browser Use. Let's explore why this happens and how to solve it.

## Understanding the Issue

Looking at [`browser_use/browser/utils/screen_resolution.py:16-26`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/utils/screen_resolution.py#L16-L26), we can see that Browser Use relies on the `screeninfo` package to get screen resolution on Windows and Linux:

```python
else:  # Windows & Linux
    try:
        from screeninfo import get_monitors

        monitors = get_monitors()
        if not monitors:
            raise Exception('No monitors detected.')
        monitor = monitors[0]
        return {'width': monitor.width, 'height': monitor.height}
    except ImportError:
        print("screeninfo package not found. Install it using 'pip install screeninfo'.")
    except Exception as e:
        print(f'Error retrieving screen resolution: {e}')
```

This code is used in [`browser_use/browser/browser.py:307-316`](https://github.com/browser-use/browser-use/blob/main/browser_use/browser/browser.py#L307-L316) during browser initialization:

```python
# Use the configured window size from new_context_config if available
if (
    not self.config.headless
    # ...other conditions...
):
    screen_size = {
        'width': self.config.new_context_config.window_width,
        'height': self.config.new_context_config.window_height,
    }
    # ...
else:
    screen_size = get_screen_resolution()
    # ...
```

## The Root Cause

The `NotImplementedError` in Windows is likely occurring because:

1. The `screeninfo` package is missing in your environment.
2. The installed `screeninfo` version might not support your specific Windows configuration.
3. There could be limitations with the Windows driver in the `screeninfo` package.

In the [pyproject.toml:32](https://github.com/browser-use/browser-use/blob/main/pyproject.toml#L32), we can see the dependency is conditionally included:

```
"screeninfo>=0.8.1; platform_system != 'darwin'",
```

## Solution Options

Here are several ways to fix this issue:

### Option 1: Install or Update screeninfo

```bash
pip install screeninfo>=0.8.1
```

### Option 2: Provide Window Size Explicitly

The most reliable solution is to specify the window dimensions directly in your BrowserConfig:

```python
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

config = BrowserConfig(
    headless=False,
    new_context_config=BrowserContextConfig(
        window_width=1920,  # Specify your desired width
        window_height=1080,  # Specify your desired height
        force_new_context=True,
    ),
)
browser = Browser(config)
```

### Option 3: Modify the Screen Resolution Function

If Options 1 and 2 don't work, you can create a modified version of the `get_screen_resolution()` function that provides fallback values for Windows:

```python
# Create a custom utility file in your project
def custom_get_screen_resolution():
    try:
        # Try to use the standard function
        from browser_use.browser.utils.screen_resolution import get_screen_resolution
        return get_screen_resolution()
    except Exception:
        # Fallback for Windows
        import platform
        if platform.system() == 'Windows':
            return {'width': 1920, 'height': 1080}
        # Re-raise for other systems
        raise
```

### Option 4: Use Headless Mode

As a workaround, you can use headless mode, which uses fixed dimensions and doesn't rely on screen detection:

```python
config = BrowserConfig(
    headless=True,  # Use headless mode
)
browser = Browser(config)
```

## Complete Working Example

Here's a full example that should work on Windows:

```python
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

# Create browser configuration with explicit window size
config = BrowserConfig(
    headless=False,
    new_context_config=BrowserContextConfig(
        window_width=1920,
        window_height=1080,
        force_new_context=True,
    ),
)

# Initialize the browser
browser = Browser(config)

# Continue with your automation
```

This approach bypasses the need for screen resolution detection entirely by providing explicit dimensions. 