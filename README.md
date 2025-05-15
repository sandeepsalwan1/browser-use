# Audio Waveform Visualizer

This script automatically fetches sound effects from Mixkit.co and creates beautiful waveform visualizations from the audio.

## Features

- Browses and downloads free sound effects from Mixkit.co
- Creates waveform visualizations of audio files
- Supports multiple visualization styles (bars, wave, outline)
- No login or authentication required
- Saves both audio files and visualizations locally

## Requirements

- Python 3.8+
- Required Python packages:
  - browser-use
  - langchain-openai
  - OpenAI API key

## Installation

1. Clone this repository or download the files.
2. Install the required Python packages:
# Audio Waveform Visualizer

This script automatically fetches sound effects from Mixkit.co and creates beautiful waveform visualizations from the audio.

## Features

- Browses and downloads free sound effects from Mixkit.co
- Creates waveform visualizations of audio files
- Supports multiple visualization styles (bars, wave, outline)
- No login or authentication required
- Saves both audio files and visualizations locally

## Requirements

- Python 3.8+
- Required Python packages:
  - browser-use
  - langchain-openai
  - OpenAI API key

## Installation

1. Clone this repository or download the files.
2. Install the required Python packages:

```bash
pip install browser-use langchain-openai
pip install browser-use langchain-openai
```

3. Set up your OpenAI API key as an environment variable:
3. Set up your OpenAI API key as an environment variable:

```bash
pip install "browser-use[memory]"
```

Install the browser:
```bash
playwright install chromium --with-deps --no-shell
```

Spin up your agent:

```python
import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
```

Add your API keys for the provider you want to use to your `.env` file.

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
GOOGLE_API_KEY=
DEEPSEEK_API_KEY=
GROK_API_KEY=
NOVITA_API_KEY=
```

For other settings, models, and more, check out the [documentation 📕](https://docs.browser-use.com).

### Test with UI

You can test browser-use using its [Web UI](https://github.com/browser-use/web-ui) or [Desktop App](https://github.com/browser-use/desktop).

### Test with an interactive CLI

You can also use our `browser-use` interactive CLI (similar to `claude` code):

```bash
pip install browser-use[cli]
browser-use
```

# Demos

<br/><br/>

[Task](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/shopping.py): Add grocery items to cart, and checkout.

[![AI Did My Groceries](https://github.com/user-attachments/assets/a0ffd23d-9a11-4368-8893-b092703abc14)](https://www.youtube.com/watch?v=L2Ya9PYNns8)

<br/><br/>

Prompt: Add my latest LinkedIn follower to my leads in Salesforce.

![LinkedIn to Salesforce](https://github.com/user-attachments/assets/50d6e691-b66b-4077-a46c-49e9d4707e07)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/find_and_apply_to_jobs.py): Read my CV & find ML jobs, save them to a file, and then start applying for them in new tabs, if you need help, ask me.'

https://github.com/user-attachments/assets/171fb4d6-0355-46f2-863e-edb04a828d04

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py): Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.

![Letter to Papa](https://github.com/user-attachments/assets/242ade3e-15bc-41c2-988f-cbc5415a66aa)

<br/><br/>

[Prompt](https://github.com/browser-use/browser-use/blob/main/examples/custom-functions/save_to_file_hugging_face.py): Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.

https://github.com/user-attachments/assets/de73ee39-432c-4b97-b4e8-939fd7f323b3

<br/><br/>

## More examples

For more examples see the [examples](examples) folder or join the [Discord](https://link.browser-use.com/discord) and show off your project. You can also see our [`awesome-prompts`](https://github.com/browser-use/awesome-prompts) repo for prompting inspiration.

# Vision

Tell your computer what to do, and it gets it done.

## Roadmap

### Agent

- [ ] Improve agent memory to handle +100 steps
- [ ] Enhance planning capabilities (load website specific context)
- [ ] Reduce token consumption (system prompt, DOM state)

### DOM Extraction

- [ ] Enable detection for all possible UI elements
- [ ] Improve state representation for UI elements so that all LLMs can understand what's on the page

### Workflows

- [ ] Let user record a workflow - which we can rerun with browser-use as a fallback
- [ ] Make rerunning of workflows work, even if pages change

### User Experience

- [ ] Create various templates for tutorial execution, job application, QA testing, social media, etc. which users can just copy & paste.
- [ ] Improve docs
- [ ] Make it faster

### Parallelization

- [ ] Human work is sequential. The real power of a browser agent comes into reality if we can parallelize similar tasks. For example, if you want to find contact information for 100 companies, this can all be done in parallel and reported back to a main agent, which processes the results and kicks off parallel subtasks again.


## Contributing

We love contributions! Feel free to open issues for bugs or feature requests. To contribute to the docs, check out the `/docs` folder.

## Local Setup

To learn more about the library, check out the [local setup 📕](https://docs.browser-use.com/development/local-setup).


`main` is the primary development branch with frequent changes. For production use, install a stable [versioned release](https://github.com/browser-use/browser-use/releases) instead.

---

## Swag

Want to show off your Browser-use swag? Check out our [Merch store](https://browsermerch.com). Good contributors will receive swag for free 👀.

## Citation

If you use Browser Use in your research or project, please cite:

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

 <div align="center"> <img src="https://github.com/user-attachments/assets/06fa3078-8461-4560-b434-445510c1766f" width="400"/> 
 
[![Twitter Follow](https://img.shields.io/twitter/follow/Gregor?style=social)](https://x.com/gregpr07)
[![Twitter Follow](https://img.shields.io/twitter/follow/Magnus?style=social)](https://x.com/mamagnus00)
 
 </div>

<div align="center">
Made with ❤️ in Zurich and San Francisco
 </div>
