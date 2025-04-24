# Browser-use Examples

This folder contains various examples demonstrating how to use the browser-use library for AI browser automation.

## Running the Examples

To run any example, first make sure you have your API key set as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

Then run the example using Python:

```bash
python simple_search.py
```

## List of Examples

- `simple_search.py`: A basic example to search the web and open a specific repository
- `github_stars.py`: Fetch the star count of the browser-use repository and summarize the project
- `weather_checker.py`: Get weather data for multiple cities and save it as JSON

## Contribute Your Examples

Have you created a cool browser automation flow? Consider contributing it to this examples folder by opening a pull request!

## Troubleshooting

If you encounter any issues:

1. Check that your API key is correctly set
2. Ensure you've installed Patchright: `patchright install chromium`
3. Check that you have the latest version of browser-use installed 