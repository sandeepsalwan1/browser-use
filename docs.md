Get Started
Quickstart
Start using Browser Use with this quickstart guide

​
Prepare the environment
Browser Use requires Python 3.11 or higher.

First, we recommend using uv to setup the Python environment.


Copy
uv venv --python 3.11
and activate it with:


Copy
# For Mac/Linux:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate
Install the dependencies:


Copy
uv pip install browser-use
Then install playwright:


Copy
uv run playwright install
​
Create an agent
Then you can use the agent as follows:

agent.py

Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
​
Set up your LLM API keys
ChatOpenAI and other Langchain chat models require API keys. You should store these in your .env file. For example, for OpenAI and Anthropic, you can set the API keys in your .env file, such as:

.env

Copy
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
For other LLM models you can refer to the Langchain documentation to find how to set them up with their specific API keys.

Was this page helpful?


Yes

No
Introduction
Supported Models
x
github
linkedin
Powered by Mintlify
Supported Models
Guide to using different LangChain chat models with Browser Use

​
Overview
Browser Use supports various LangChain chat models. Here’s how to configure and use the most popular ones. The full list is available in the LangChain documentation.

​
Model Recommendations
We have yet to test performance across all models. Currently, we achieve the best results using GPT-4o with an 89% accuracy on the WebVoyager Dataset. DeepSeek-V3 is 30 times cheaper than GPT-4o. Gemini-2.0-exp is also gaining popularity in the community because it is currently free. We also support local models, like Qwen 2.5, but be aware that small models often return the wrong output structure-which lead to parsing errors. We believe that local models will improve significantly this year.

All models require their respective API keys. Make sure to set them in your environment variables before running the agent.

​
Supported Models
All LangChain chat models, which support tool-calling are available. We will document the most popular ones here.

​
OpenAI
OpenAI’s GPT-4o models are recommended for best performance.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Initialize the model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
Required environment variables:

.env

Copy
OPENAI_API_KEY=
​
Anthropic

Copy
from langchain_anthropic import ChatAnthropic
from browser_use import Agent

# Initialize the model
llm = ChatAnthropic(
    model_name="claude-3-5-sonnet-20240620",
    temperature=0.0,
    timeout=100, # Increase for complex tasks
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
And add the variable:

.env

Copy
ANTHROPIC_API_KEY=
​
Azure OpenAI

Copy
from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
import os

# Initialize the model
llm = AzureChatOpenAI(
    model="gpt-4o",
    api_version='2024-10-21',
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
    api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
Required environment variables:

.env

Copy
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_KEY=
​
Gemini

Copy
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

# Read GEMINI_API_KEY into env
load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
Required environment variables:

.env

Copy
GEMINI_API_KEY=
​
DeepSeek-V3
The community likes DeepSeek-V3 for its low price, no rate limits, open-source nature, and good performance. The example is available here.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
Required environment variables:

.env

Copy
DEEPSEEK_API_KEY=
​
DeepSeek-R1
We support DeepSeek-R1. Its not fully tested yet, more and more functionality will be added, like e.g. the output of it’sreasoning content. The example is available here. It does not support vision. The model is open-source so you could also use it with Ollama, but we have not tested it.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize the model
llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-reasoner', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
Required environment variables:

.env

Copy
DEEPSEEK_API_KEY=
​
Ollama
Many users asked for local models. Here they are.

Download Ollama from here
Run ollama pull model_name. Pick a model which supports tool-calling from here
Run ollama start

Copy
from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr


# Initialize the model
llm=ChatOllama(model="qwen2.5", num_ctx=32000)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm
)
Required environment variables: None!

​
Novita AI
Novita AI is an LLM API provider that offers a wide range of models. Note: choose a model that supports function calling.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("NOVITA_API_KEY")

# Initialize the model
llm = ChatOpenAI(base_url='https://api.novita.ai/v3/openai', model='deepseek/deepseek-v3-0324', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
Required environment variables:

.env

Copy
NOVITA_API_KEY=
​
X AI
X AI is an LLM API provider that offers a wide range of models. Note: choose a model that supports function calling.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROK_API_KEY")

# Initialize the model
llm = ChatOpenAI(
    base_url='https://api.x.ai/v1',
    model='grok-3-beta',
    api_key=SecretStr(api_key)
)

# Create agent with the model
agent = Agent(
    task="Your task here",
    llm=llm,
    use_vision=False
)
Required environment variables:

.env

Copy
GROK_API_KEY=
​
Coming soon
(We are working on it)

Groq
Github
Fine-tuned models



Agent Settings
Learn how to configure the agent

​
Overview
The Agent class is the core component of Browser Use that handles browser automation. Here are the main configuration options you can use when initializing an agent.

​
Basic Settings

Copy
from browser_use import Agent
from langchain_openai import ChatOpenAI

agent = Agent(
    task="Search for latest news about AI",
    llm=ChatOpenAI(model="gpt-4o"),
)
​
Required Parameters
task: The instruction for the agent to execute
llm: A LangChain chat model instance. See LangChain Models for supported models.
​
Agent Behavior
Control how the agent operates:


Copy
agent = Agent(
    task="your task",
    llm=llm,
    controller=custom_controller,  # For custom tool calling
    use_vision=True,              # Enable vision capabilities
    save_conversation_path="logs/conversation"  # Save chat logs
)
​
Behavior Parameters
controller: Registry of functions the agent can call. Defaults to base Controller. See Custom Functions for details.
use_vision: Enable/disable vision capabilities. Defaults to True.
When enabled, the model processes visual information from web pages
Disable to reduce costs or use models without vision support
For GPT-4o, image processing costs approximately 800-1000 tokens (~$0.002 USD) per image (but this depends on the defined screen size)
save_conversation_path: Path to save the complete conversation history. Useful for debugging.
override_system_message: Completely replace the default system prompt with a custom one.
extend_system_message: Add additional instructions to the default system prompt.
Vision capabilities are recommended for better web interaction understanding, but can be disabled to reduce costs or when using models without vision support.

​
(Reuse) Browser Configuration
You can configure how the agent interacts with the browser. To see more Browser options refer to the Browser Settings documentation.

​
Reuse Existing Browser
browser: A Browser Use Browser instance. When provided, the agent will reuse this browser instance and automatically create new contexts for each run().


Copy
from browser_use import Agent, Browser
from browser_use.browser.context import BrowserContext

# Reuse existing browser
browser = Browser()
agent = Agent(
    task=task1,
    llm=llm,
    browser=browser  # Browser instance will be reused
)

await agent.run()

# Manually close the browser
await browser.close()
Remember: in this scenario the Browser will not be closed automatically.

​
Reuse Existing Browser Context
browser_context: A Playwright browser context. Useful for maintaining persistent sessions. See Persistent Browser for more details.


Copy
from browser_use import Agent, Browser
from playwright.async_api import BrowserContext

# Use specific browser context (preferred method)
async with await browser.new_context() as context:
    agent = Agent(
        task=task2,
        llm=llm,
        browser_context=context  # Use persistent context
    )

    # Run the agent
    await agent.run()

    # Pass the context to the next agent
    next_agent = Agent(
        task=task2,
        llm=llm,
        browser_context=context
    )

    ...

await browser.close()
For more information about how browser context works, refer to the Playwright documentation.

You can reuse the same context for multiple agents. If you do nothing, the browser will be automatically created and closed on run() completion.

​
Running the Agent
The agent is executed using the async run() method:

max_steps (default: 100) Maximum number of steps the agent can take during execution. This prevents infinite loops and helps control execution time.
​
Agent History
The method returns an AgentHistoryList object containing the complete execution history. This history is invaluable for debugging, analysis, and creating reproducible scripts.


Copy
# Example of accessing history
history = await agent.run()

# Access (some) useful information
history.urls()              # List of visited URLs
history.screenshots()       # List of screenshot paths
history.action_names()      # Names of executed actions
history.extracted_content() # Content extracted during execution
history.errors()           # Any errors that occurred
history.model_actions()     # All actions with their parameters
The AgentHistoryList provides many helper methods to analyze the execution:

final_result(): Get the final extracted content
is_done(): Check if the agent completed successfully
has_errors(): Check if any errors occurred
model_thoughts(): Get the agent’s reasoning process
action_results(): Get results of all actions
For a complete list of helper methods and detailed history analysis capabilities, refer to the AgentHistoryList source code.

​
Run initial actions without LLM
With this example you can run initial actions without the LLM. Specify the action as a dictionary where the key is the action name and the value is the action parameters. You can find all our actions in the Controller source code.


Copy

initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
]
agent = Agent(
	task='What theories are displayed on the page?',
	initial_actions=initial_actions,
	llm=llm,
)
​
Run with message context
You can configure the agent and provide a separate message to help the LLM understand the task better.


Copy
from langchain_openai import ChatOpenAI

agent = Agent(
    task="your task",
    message_context="Additional information about the task",
    llm = ChatOpenAI(model='gpt-4o')
)
​
Run with planner model
You can configure the agent to use a separate planner model for high-level task planning:


Copy
from langchain_openai import ChatOpenAI

# Initialize models
llm = ChatOpenAI(model='gpt-4o')
planner_llm = ChatOpenAI(model='o3-mini')

agent = Agent(
    task="your task",
    llm=llm,
    planner_llm=planner_llm,           # Separate model for planning
    use_vision_for_planner=False,      # Disable vision for planner
    planner_interval=4                 # Plan every 4 steps
)
​
Planner Parameters
planner_llm: A LangChain chat model instance used for high-level task planning. Can be a smaller/cheaper model than the main LLM.
use_vision_for_planner: Enable/disable vision capabilities for the planner model. Defaults to True.
planner_interval: Number of steps between planning phases. Defaults to 1.
Using a separate planner model can help:

Reduce costs by using a smaller model for high-level planning
Improve task decomposition and strategic thinking
Better handle complex, multi-step tasks
The planner model is optional. If not specified, the agent will not use the planner model.

​
Optional Parameters
message_context: Additional information about the task to help the LLM understand the task better.
initial_actions: List of initial actions to run before the main task.
max_actions_per_step: Maximum number of actions to run in a step. Defaults to 10.
max_failures: Maximum number of failures before giving up. Defaults to 3.
retry_delay: Time to wait between retries in seconds when rate limited. Defaults to 10.
generate_gif: Enable/disable GIF generation. Defaults to False. Set to True or a string path to save the GIF.
​
Memory Management
Browser Use includes a procedural memory system using Mem0 that automatically summarizes the agent’s conversation history at regular intervals to optimize context window usage during long tasks.


Copy
from browser_use.agent.memory import MemoryConfig

agent = Agent(
    task="your task",
    llm=llm,
    enable_memory=True,
    memory_config=MemoryConfig(
        agent_id="my_custom_agent",
        memory_interval=15
    )
)
​
Memory Parameters
enable_memory: Enable/disable the procedural memory system. Defaults to True.
memory_config: A MemoryConfig Pydantic model instance (required). Dictionary format is not supported.
​
Using MemoryConfig
You must configure the memory system using the MemoryConfig Pydantic model for a type-safe approach:


Copy
from browser_use.agent.memory import MemoryConfig

agent = Agent(
    task=task_description,
    llm=llm,
    memory_config=MemoryConfig(
        agent_id="my_agent",
        memory_interval=15,
        embedder_provider="openai",
        embedder_model="text-embedding-3-large",
        embedder_dims=1536,
    )
)
The MemoryConfig model provides these configuration options:

​
Memory Settings
agent_id: Unique identifier for the agent (default: "browser_use_agent")
memory_interval: Number of steps between memory summarization (default: 10)
​
Embedder Settings
embedder_provider: Provider for embeddings ('openai', 'gemini', 'ollama', or 'huggingface')
embedder_model: Model name for the embedder
embedder_dims: Dimensions for the embeddings
​
Vector Store Settings
vector_store_provider: Provider for vector storage (currently only 'faiss' is supported)
vector_store_base_path: Path for storing vector data (e.g. /tmp/mem0)
The model automatically sets appropriate defaults based on the LLM being used:

For ChatOpenAI: Uses OpenAI’s text-embedding-3-small embeddings
For ChatGoogleGenerativeAI: Uses Gemini’s models/text-embedding-004 embeddings
For ChatOllama: Uses Ollama’s nomic-embed-text embeddings
Default: Uses Hugging Face’s all-MiniLM-L6-v2 embeddings
Always pass a properly constructed MemoryConfig object to the memory_config parameter. Dictionary-based configuration is no longer supported.

​
How Memory Works
When enabled, the agent periodically compresses its conversation history into concise summaries:

Every memory_interval steps, the agent reviews its recent interactions
It creates a procedural memory summary using the same LLM as the agent
The original messages are replaced with the summary, reducing token usage
This process helps maintain important context while freeing up the context window
​
Disabling Memory
If you want to disable the memory system (for debugging or for shorter tasks), set enable_memory to False:


Copy
agent = Agent(
    task="your task",
    llm=llm,
    enable_memory=False
)
Disabling memory may be useful for debugging or short tasks, but for longer tasks, it can lead to context window overflow as the conversation history grows. The memory system helps maintain performance during extended sessions.

Customize
Browser Settings
Configure browser behavior and context settings

Browser Use allows you to customize the browser’s behavior through two main configuration classes: BrowserConfig and BrowserContextConfig. These settings control everything from headless mode to proxy settings and page load behavior.

We are currently working on improving how browser contexts are managed. The system will soon transition to a “1 agent, 1 browser, 1 context” model for better stability and developer experience.

​
Browser Configuration
The BrowserConfig class controls the core browser behavior and connection settings.


Copy
from browser_use import BrowserConfig

# Basic configuration
config = BrowserConfig(
    headless=False,
    disable_security=False
)

browser = Browser(config=config)

agent = Agent(
    browser=browser,
    # ...
)
​
Core Settings
headless (default: False) Runs the browser without a visible UI. Note that some websites may detect headless mode.

disable_security (default: False) Disables browser security features. While this can fix certain functionality issues (like cross-site iFrames), it should be used cautiously, especially when visiting untrusted websites.

keep_alive (default: False) Keeps the browser alive after the agent has finished running. This is useful when you need to run multiple tasks with the same browser instance.

​
Additional Settings
extra_browser_args (default: []) Additional arguments are passed to the browser at launch. See the full list of available arguments.

proxy (default: None) Standard Playwright proxy settings for using external proxy services.

new_context_config (default: BrowserContextConfig()) Default settings for new browser contexts. See Context Configuration below.

For web scraping tasks on sites that restrict automated access, we recommend using external browser or proxy providers for better reliability.

​
Alternative Initialization
These settings allow you to connect to external browser providers or use a local Chrome instance.

​
External Browser Provider (wss)
Connect to cloud-based browser services for enhanced reliability and proxy capabilities.


Copy
config = BrowserConfig(
    wss_url="wss://your-browser-provider.com/ws"
)
wss_url (default: None) WebSocket URL for connecting to external browser providers (e.g., anchorbrowser.io, steel.dev, browserbase.com, browserless.io, TestingBot).
This overrides local browser settings and uses the provider’s configuration. Refer to their documentation for settings.

​
External Browser Provider (cdp)
Connect to cloud or local Chrome instances using Chrome DevTools Protocol (CDP) for use with tools like headless-shell or browserless.


Copy
config = BrowserConfig(
    cdp_url="http://localhost:9222"
)
cdp_url (default: None) URL for connecting to a Chrome instance via CDP. Commonly used for debugging or connecting to locally running Chrome instances.
​
Local Chrome Instance (binary)
Connect to your existing Chrome installation to access saved states and cookies.


Copy
config = BrowserConfig(
    browser_binary_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
browser_binary_path (default: None) Path to connect to an existing Browser installation. Particularly useful for workflows requiring existing login states or browser preferences.
This will overwrite other browser settings.
​
Context Configuration
The BrowserContextConfig class controls settings for individual browser contexts.


Copy
from browser_use.browser.context import BrowserContextConfig

config = BrowserContextConfig(
    cookies_file="path/to/cookies.json",
    wait_for_network_idle_page_load_time=3.0,
    window_width=1280,
    window_height=1100,
    locale='en-US',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    highlight_elements=True,
    viewport_expansion=500,
    allowed_domains=['google.com', 'wikipedia.org'],
)

browser = Browser()
context = BrowserContext(browser=browser, config=config)


async def run_search():
	agent = Agent(
		browser_context=context,
		task='Your task',
		llm=llm)
​
Configuration Options
​
Page Load Settings
minimum_wait_page_load_time (default: 0.5) Minimum time to wait before capturing page state for LLM input.

wait_for_network_idle_page_load_time (default: 1.0) Time to wait for network activity to cease. Increase to 3-5s for slower websites. This tracks essential content loading, not dynamic elements like videos.

maximum_wait_page_load_time (default: 5.0) Maximum time to wait for page load before proceeding.

​
Display Settings
window_width (default: 1280) and window_height (default: 1100) Browser window dimensions. The default size is optimized for general use cases and interaction with common UI elements like cookie banners.

locale (default: None) Specify user locale, for example en-GB, de-DE, etc. Locale will affect the navigator. Language value, Accept-Language request header value as well as number and date formatting rules. If not provided, defaults to the system default locale.

highlight_elements (default: True) Highlight interactive elements on the screen with colorful bounding boxes.

viewport_expansion (default: 500) Viewport expansion in pixels. With this you can control how much of the page is included in the context of the LLM. Setting this parameter controls the highlighting of elements:

-1: All elements from the entire page will be included, regardless of visibility (highest token usage but most complete).
0: Only elements which are currently visible in the viewport will be included.
500 (default): Elements in the viewport plus an additional 500 pixels in each direction will be included, providing a balance between context and token usage.
​
Restrict URLs
allowed_domains (default: None) List of allowed domains that the agent can access. If None, all domains are allowed. Example: [‘google.com’, ‘wikipedia.org’] - Here the agent will only be able to access google and wikipedia.
​
Session Management
keep_alive (default: False) Keeps the browser context (tab/session) alive after an agent task has completed. This is useful for maintaining session state across multiple tasks.
​
Debug and Recording
save_recording_path (default: None) Directory path for saving video recordings.

trace_path (default: None) Directory path for saving trace files. Files are automatically named as {trace_path}/{context_id}.zip.

save_playwright_script_path (default: None) BETA: Filename to save a replayable playwright python script to containing the steps the agent took.

Was this page helpful?


Connect to your Browser
With this you can connect to your real browser, where you are logged in with all your accounts.

​
Overview
You can connect the agent to your real Chrome browser instance, allowing it to access your existing browser profile with all your logged-in accounts and settings. This is particularly useful when you want the agent to interact with services where you’re already authenticated.

First make sure to close all running Chrome instances.

​
Basic Configuration
To connect to your real Chrome browser, you’ll need to specify the path to your Chrome executable when creating the Browser instance:


Copy
from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import asyncio
# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# Create the agent with your configured browser
agent = Agent(
    task="Your task here",
    llm=ChatOpenAI(model='gpt-4o'),
    browser=browser,
)

async def main():
    await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
When using your real browser, the agent will have access to all your logged-in sessions. Make sure to ALWAYS review the task you’re giving to the agent and ensure it 

Output Format
The default is text. But you can define a structured output format to make post-processing easier.

​
Custom output format
With this example you can define what output format the agent should return to you.


Copy
from pydantic import BaseModel
# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int


class Posts(BaseModel):
	posts: List[Post]


controller = Controller(output_model=Posts)


async def main():
	task = 'Go to hackernews show hn and give me the first  5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print('\n--------------------------------')
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
	else:
		print('No result')


if __name__ == '__main__':
	asyncio.run(main())



\ystem Prompt
Customize the system prompt to control agent behavior and capabilities

​
Overview
You can customize the system prompt in two ways:

Extend the default system prompt with additional instructions
Override the default system prompt entirely
Custom system prompts allow you to modify the agent’s behavior at a fundamental level. Use this feature carefully as it can significantly impact the agent’s performance and reliability.

​
Extend System Prompt (recommended)
To add additional instructions to the default system prompt:


Copy
extend_system_message = """
REMEMBER the most important RULE:
ALWAYS open first a new tab and go first to url wikipedia.com no matter the task!!!
"""
​
Override System Prompt
Not recommended! If you must override the default system prompt, make sure to test the agent yourself.

Anyway, to override the default system prompt:


Copy
# Define your complete custom prompt
override_system_message = """
You are an AI agent that helps users with web browsing tasks.

[Your complete custom instructions here...]
"""

# Create agent with custom system prompt
agent = Agent(
    task="Your task here",
    llm=ChatOpenAI(model='gpt-4'),
    override_system_message=override_system_message
)
​
Extend Planner System Prompt
You can customize the behavior of the planning agent by extending its system prompt:


Copy
extend_planner_system_message = """
PRIORITIZE gathering information before taking any action.
Always suggest exploring multiple options before making a decision.
"""

# Create agent with extended planner system prompt
llm = ChatOpenAI(model='gpt-4o')
planner_llm = ChatOpenAI(model='gpt-4o-mini')

agent = Agent(
	task="Your task here",
	llm=llm,
	planner_llm=planner_llm,
	extend_planner_system_message=extend_planner_system_message
)


Sensitive Data
Handle sensitive information securely by preventing the model from seeing actual passwords.

​
Handling Sensitive Data
When working with sensitive information like passwords, you can use the sensitive_data parameter to prevent the model from seeing the actual values while still allowing it to reference them in its actions.

Make sure to always set allowed_domains to restrict the domains the Agent is allowed to visit when working with sensitive data or logins.

Here’s an example of how to use sensitive data:


Copy
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.0,
)

# Define sensitive data
# The model will only see the keys (x_name, x_password) but never the actual values
sensitive_data = {'x_name': 'magnus', 'x_password': '12345678'}

# Use the placeholder names in your task description
task = 'go to x.com and login with x_name and x_password then write a post about the meaning of life'

# Pass the sensitive data to the agent
agent = Agent(
    task=task,
    llm=llm,
    sensitive_data=sensitive_data,
    browser=Browser(
        config=BrowserConfig(
            allowed_domains=['example.com'],  # domains that the agent should be restricted to
        ),
    )
)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
In this example:

The model only sees x_name and x_password as placeholders.
When the model wants to use your password it outputs x_password - and we replace it with the actual value.
When your password is visible on the current page, we replace it in the LLM input - so that the model never has it in its state.
The agent will be prevented from going to any site not on example.com to protect from prompt injection attacks and jailbreaks
​
Missing or Empty Values
When working with sensitive data, keep these details in mind:

If a key referenced by the model (<secret>key_name</secret>) is missing from your sensitive_data dictionary, a warning will be logged but the substitution tag will be preserved.
If you provide an empty value for a key in the sensitive_data dictionary, it will be treated the same as a missing key.
The system will always attempt to process all valid substitutions, even if some keys are missing or empty.
Warning: Vision models still see the image of the page - where the sensitive data might be visible.

This approach ensures that sensitive information remains secure while still allowing the agent to perform tasks that require authentication.


Custom Functions
Extend default agent and write custom function calls

​
Basic Function Registration
Functions can be either sync or async. Keep them focused and single-purpose.


Copy
from browser_use import Controller, ActionResult
# Initialize the controller
controller = Controller()

@controller.action('Ask user for information')
def ask_human(question: str) -> str:
    answer = input(f'\n{question}\nInput: ')
    return ActionResult(extracted_content=answer)
Basic Controller has all basic functionality you might need to interact with the browser already implemented.


Copy
# ... then pass controller to the agent
agent = Agent(
    task=task,
    llm=llm,
    controller=controller
)
Keep the function name and description short and concise. The Agent use the function solely based on the name and description. The stringified output of the action is passed to the Agent.

​
Browser-Aware Functions
For actions that need browser access, simply add the browser parameter inside the function parameters:

Please note that browser-use’s Browser class is a wrapper class around Playwright’s Browser. The Browser.playwright_browser attr can be used to directly access the Playwright browser object if needed.


Copy
from browser_use import Browser, Controller, ActionResult

controller = Controller()
@controller.action('Open website')
async def open_website(url: str, browser: Browser):
    page = await browser.get_current_page()
    await page.goto(url)
    return ActionResult(extracted_content='Website opened')
​
Structured Parameters with Pydantic
For complex actions, you can define parameter schemas using Pydantic models:


Copy
from pydantic import BaseModel
from typing import Optional
from browser_use import Controller, ActionResult, Browser

controller = Controller()

class JobDetails(BaseModel):
    title: str
    company: str
    job_link: str
    salary: Optional[str] = None

@controller.action(
    'Save job details which you found on page',
    param_model=JobDetails
)
async def save_job(params: JobDetails, browser: Browser):
    print(f"Saving job: {params.title} at {params.company}")

    # Access browser if needed
    page = browser.get_current_page()
    await page.goto(params.job_link)
​
Using Custom Actions with multiple agents
You can use the same controller for multiple agents.


Copy
controller = Controller()

# ... register actions to the controller

agent = Agent(
    task="Go to website X and find the latest news",
    llm=llm,
    controller=controller
)

# Run the agent
await agent.run()

agent2 = Agent(
    task="Go to website Y and find the latest news",
    llm=llm,
    controller=controller
)

await agent2.run()
The controller is stateless and can be used to register multiple actions and multiple agents.

​
Exclude functions
If you want less actions to be used by the agent, you can exclude them from the controller.


Copy
controller = Controller(exclude_actions=['open_tab', 'search_google'])
For more examples like file upload or notifications, visit examples/custom-functions.

Lifecycle Hooks
Customize agent behavior with lifecycle hooks

​
Using Agent Lifecycle Hooks
Browser-Use provides lifecycle hooks that allow you to execute custom code at specific points during the agent’s execution. These hooks enable you to capture detailed information about the agent’s actions, modify behavior, or integrate with external systems.

​
Available Hooks
Currently, Browser-Use provides the following hooks:

Hook	Description	When it’s called
on_step_start	Executed at the beginning of each agent step	Before the agent processes the current state and decides on the next action
on_step_end	Executed at the end of each agent step	After the agent has executed the action for the current step
​
Using Hooks
Hooks are passed as parameters to the agent.run() method. Each hook should be a callable function that accepts the agent instance as its parameter.

​
Basic Example

Copy
from browser_use import Agent
from langchain_openai import ChatOpenAI


async def my_step_hook(agent):
    # inside a hook you can access all the state and methods under the Agent object:
    #   agent.settings, agent.state, agent.task
    #   agent.controller, agent.llm, agent.browser, agent.browser_context
    #   agent.pause(), agent.resume(), agent.add_new_task(...), etc.
    
    current_page = await agent.browser_context.get_current_page()
    
    visit_log = agent.state.history.urls()
    current_url = current_page.url
    previous_url = visit_log[-2] if len(visit_log) >= 2 else None
    print(f"Agent was last on URL: {previous_url} and is now on {current_url}")
    
    # You also have direct access to the playwright Page and Browser Context
    #   https://playwright.dev/python/docs/api/class-page

    # Example: listen for events on the page, interact with the DOM, run JS directly, etc.
    await current_page.on('domcontentloaded', async lambda: print('page navigated to a new url...'))
    await current_page.locator("css=form > input[type=submit]").click()
    await current_page.evaluate('() => alert(1)')
    await agent.browser_context.session.context.add_init_script('/* some JS to run on every page */')
    
    # Example: monitor or intercept all network requests
    async def handle_request(route):
		# Print, modify, block, etc. do anything to the requests here
        #   https://playwright.dev/python/docs/network#handle-requests
		print(route.request, route.request.headers)
		await route.continue_(headers=route.request.headers)
	await current_page.route("**/*", handle_route)

    # Example: pause agent execution and resume it based on some custom code
    if '/completed' in current_url:
        agent.pause()
        Path('result.txt').write_text(await current_page.content()) 
        input('Saved "completed" page content to result.txt, press [Enter] to resume...')
        agent.resume()
    
agent = Agent(
    task="Search for the latest news about AI",
    llm=ChatOpenAI(model="gpt-4o"),
)

await agent.run(
    on_step_start=my_step_hook,
    # on_step_end=...
    max_steps=10
)
​
Complete Example: Agent Activity Recording System
This comprehensive example demonstrates a complete implementation for recording and saving Browser-Use agent activity, consisting of both server and client components.

​
Setup Instructions
To use this example, you’ll need to:

Set up the required dependencies:


Copy
pip install fastapi uvicorn prettyprinter pyobjtojson dotenv browser-use langchain-openai
Create two separate Python files:

api.py - The FastAPI server component
client.py - The Browser-Use agent with recording hook
Run both components:

Start the API server first: python api.py
Then run the client: python client.py
​
Server Component (api.py)
The server component handles receiving and storing the agent’s activity data:


Copy
#!/usr/bin/env python3

#
# FastAPI API to record and save Browser-Use activity data.
# Save this code to api.py and run with `python api.py`
# 

import json
import base64
from pathlib import Path

from fastapi import FastAPI, Request
import prettyprinter
import uvicorn

prettyprinter.install_extras()

# Utility function to save screenshots
def b64_to_png(b64_string: str, output_file):
    """
    Convert a Base64-encoded string to a PNG file.
    
    :param b64_string: A string containing Base64-encoded data
    :param output_file: The path to the output PNG file
    """
    with open(output_file, "wb") as f:
        f.write(base64.b64decode(b64_string))

# Initialize FastAPI app
app = FastAPI()


@app.post("/post_agent_history_step")
async def post_agent_history_step(request: Request):
    data = await request.json()
    prettyprinter.cpprint(data)

    # Ensure the "recordings" folder exists using pathlib
    recordings_folder = Path("recordings")
    recordings_folder.mkdir(exist_ok=True)

    # Determine the next file number by examining existing .json files
    existing_numbers = []
    for item in recordings_folder.iterdir():
        if item.is_file() and item.suffix == ".json":
            try:
                file_num = int(item.stem)
                existing_numbers.append(file_num)
            except ValueError:
                # In case the file name isn't just a number
                pass

    if existing_numbers:
        next_number = max(existing_numbers) + 1
    else:
        next_number = 1

    # Construct the file path
    file_path = recordings_folder / f"{next_number}.json"

    # Save the JSON data to the file
    with file_path.open("w") as f:
        json.dump(data, f, indent=2)

    # Optionally save screenshot if needed
    # if "website_screenshot" in data and data["website_screenshot"]:
    #     screenshot_folder = Path("screenshots")
    #     screenshot_folder.mkdir(exist_ok=True)
    #     b64_to_png(data["website_screenshot"], screenshot_folder / f"{next_number}.png")

    return {"status": "ok", "message": f"Saved to {file_path}"}

if __name__ == "__main__":
    print("Starting Browser-Use recording API on http://0.0.0.0:9000")
    uvicorn.run(app, host="0.0.0.0", port=9000)
​
Client Component (client.py)
The client component runs the Browser-Use agent with a recording hook:


Copy
#!/usr/bin/env python3

#
# Client to record and save Browser-Use activity.
# Save this code to client.py and run with `python client.py`
#

import asyncio
import requests
from dotenv import load_dotenv
from pyobjtojson import obj_to_json
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Load environment variables (for API keys)
load_dotenv()


def send_agent_history_step(data):
    """Send the agent step data to the recording API"""
    url = "http://127.0.0.1:9000/post_agent_history_step"
    response = requests.post(url, json=data)
    return response.json()


async def record_activity(agent_obj):
    """Hook function that captures and records agent activity at each step"""
    website_html = None
    website_screenshot = None
    urls_json_last_elem = None
    model_thoughts_last_elem = None
    model_outputs_json_last_elem = None
    model_actions_json_last_elem = None
    extracted_content_json_last_elem = None

    print('--- ON_STEP_START HOOK ---')
    
    # Capture current page state
    website_html = await agent_obj.browser_context.get_page_html()
    website_screenshot = await agent_obj.browser_context.take_screenshot()

    # Make sure we have state history
    if hasattr(agent_obj, "state"):
        history = agent_obj.state.history
    else:
        history = None
        print("Warning: Agent has no state history")
        return

    # Process model thoughts
    model_thoughts = obj_to_json(
        obj=history.model_thoughts(),
        check_circular=False
    )
    if len(model_thoughts) > 0:
        model_thoughts_last_elem = model_thoughts[-1]

    # Process model outputs
    model_outputs = agent_obj.state.history.model_outputs()
    model_outputs_json = obj_to_json(
        obj=model_outputs,
        check_circular=False
    )
    if len(model_outputs_json) > 0:
        model_outputs_json_last_elem = model_outputs_json[-1]

    # Process model actions
    model_actions = agent_obj.state.history.model_actions()
    model_actions_json = obj_to_json(
        obj=model_actions,
        check_circular=False
    )
    if len(model_actions_json) > 0:
        model_actions_json_last_elem = model_actions_json[-1]

    # Process extracted content
    extracted_content = agent_obj.state.history.extracted_content()
    extracted_content_json = obj_to_json(
        obj=extracted_content,
        check_circular=False
    )
    if len(extracted_content_json) > 0:
        extracted_content_json_last_elem = extracted_content_json[-1]

    # Process URLs
    urls = agent_obj.state.history.urls()
    urls_json = obj_to_json(
        obj=urls,
        check_circular=False
    )
    if len(urls_json) > 0:
        urls_json_last_elem = urls_json[-1]

    # Create a summary of all data for this step
    model_step_summary = {
        "website_html": website_html,
        "website_screenshot": website_screenshot,
        "url": urls_json_last_elem,
        "model_thoughts": model_thoughts_last_elem,
        "model_outputs": model_outputs_json_last_elem,
        "model_actions": model_actions_json_last_elem,
        "extracted_content": extracted_content_json_last_elem
    }

    print("--- MODEL STEP SUMMARY ---")
    print(f"URL: {urls_json_last_elem}")
    
    # Send data to the API
    result = send_agent_history_step(data=model_step_summary)
    print(f"Recording API response: {result}")


async def run_agent():
    """Run the Browser-Use agent with the recording hook"""
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    
    try:
        print("Starting Browser-Use agent with recording hook")
        await agent.run(
            on_step_start=record_activity,
            max_steps=30
        )
    except Exception as e:
        print(f"Error running agent: {e}")


if __name__ == "__main__":
    # Check if API is running
    try:
        requests.get("http://127.0.0.1:9000")
        print("Recording API is available")
    except:
        print("Warning: Recording API may not be running. Start api.py first.")
    
    # Run the agent
    asyncio.run(run_agent())
​
Working with the Recorded Data
After running the agent, you’ll find the recorded data in the recordings directory. Here’s how you can use this data:

View recorded sessions: Each JSON file contains a snapshot of agent activity for one step
Extract screenshots: You can modify the API to save screenshots separately
Analyze agent behavior: Use the recorded data to study how the agent navigates websites
​
Extending the Example
You can extend this recording system in several ways:

Save screenshots separately: Uncomment the screenshot saving code in the API
Add a web dashboard: Create a simple web interface to view recorded sessions
Add session IDs: Modify the API to group steps by agent session
Add filtering: Implement filters to record only specific types of actions
​
Data Available in Hooks
When working with agent hooks, you have access to the entire agent instance. Here are some useful data points you can access:

agent.state.history.model_thoughts(): Reasoning from Browser Use’s model.
agent.state.history.model_outputs(): Raw outputs from the Browsre Use’s model.
agent.state.history.model_actions(): Actions taken by the agent
agent.state.history.extracted_content(): Content extracted from web pages
agent.state.history.urls(): URLs visited by the agent
agent.browser_context.get_page_html(): Current page HTML
agent.browser_context.take_screenshot(): Screenshot of the current page
​
Tips for Using Hooks
Avoid blocking operations: Since hooks run in the same execution thread as the agent, try to keep them efficient or use asynchronous patterns.
Handle exceptions: Make sure your hook functions handle exceptions gracefully to prevent interrupting the agent’s main flow.
Consider storage needs: When capturing full HTML and screenshots, be mindful of storage requirements.


Evaluations
Test the Browser Use agent on standardized benchmarks

​
Prerequisites
Browser Use uses proprietary/private test sets that must never be committed to Github and must be fetched through a authorized api request. Accessing these test sets requires an approved Browser Use account. There are currently no publicly available test sets, but some may be released in the future.

​
Get an Api Access Key
First, navigate to https://browser-use.tools and log in with an authorized browser use account.

Then, click the “Account” button at the top right of the page, and click the “Cycle New Key” button on that page.

Copy the resulting url and secret key into your .env file. It should look like this:

.env

Copy
EVALUATION_TOOL_URL= ...
EVALUATION_TOOL_SECRET_KEY= ...
​
Running Evaluations
First, ensure your file eval/service.py is up to date.

Then run the file:


Copy
python eval/service.py
​
Configuring Evaluations
You can modify the evaluation by providing flags to the evaluation script. For instance:


Copy
python eval/service.py --parallel_runs 5 --parallel_evaluations 5 --max-steps 25 --start 0 --end 100 --model gpt-4o
The evaluations webpage has a convenient GUI for generating these commands. To use it, navigate to https://browser-use.tools/dashboard.

Then click the button “New Eval Run” on the left panel. This will open a interface with selectors, inputs, sliders, and switches.

Input your desired configuration into the interface and copy the resulting python command at the bottom. Then run this command as before.

Observability
Trace Browser Use’s agent execution steps and browser sessions

​
Overview
Browser Use has a native integration with Laminar - open-source platform for tracing, evals and labeling of AI agents. Read more about Laminar in the Laminar docs.

Laminar excels at tracing browser agents by providing unified visibility into both browser session recordings and agent execution steps.

​
Setup
To setup Laminar, you need to install the lmnr package and set the LMNR_PROJECT_API_KEY environment variable.

To get your project API key, you can either:

Register on Laminar Cloud and get the key from your project settings
Or spin up a local Laminar instance and get the key from the settings page

Copy
pip install 'lmnr[all]'
export LMNR_PROJECT_API_KEY=<your-project-api-key>
​
Usage
Then, you simply initialize the Laminar at the top of your project and both Browser Use and session recordings will be automatically traced.


Copy
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

from lmnr import Laminar
# this line auto-instruments Browser Use and any browser you use (local or remote)
Laminar.initialize(project_api_key="...") # you can also pass project api key here

async def main():
    agent = Agent(
        task="open google, search Laminar AI",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
​
Viewing Traces
You can view traces in the Laminar UI by going to the traces tab in your project. When you select a trace, you can see both the browser session recording and the agent execution steps.

Timeline of the browser session is synced with the agent execution steps, timeline highlights indicate the agent’s current step synced with the browser session. In the trace view, you can also see the agent’s current step, the tool it’s using, and the tool’s input and output. Tools are highlighted in the timeline with a yellow color.

Laminar
​
Laminar
To learn more about tracing and evaluating your browser agents, check out the Laminar docs. 


Basic Examples
Simple
Find the cheapest flight between two cities using Kayak.

import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.0,
)
task = 'Go to kayak.com and find the cheapest flight from Zurich to San Francisco on 2025-05-01'

agent = Agent(task=task, llm=llm)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Browser
Real Browser
Configure and use a real Chrome browser instance for an agent by specifying the browser binary path.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

browser = Browser(
	config=BrowserConfig(
		browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

async def main():
	agent = Agent(
		task='In docs.google.com write my Papa a quick letter',
		llm=ChatOpenAI(model='gpt-4o'),
		browser=browser,
	)

	await agent.run()
	await browser.close()

if __name__ == '__main__':
	asyncio.run(main())
View full example

Stealth
Configure browser settings to avoid bot detection on websites.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig

llm = ChatOpenAI(model='gpt-4o')
browser = Browser(
	config=BrowserConfig(
		headless=False,
		disable_security=False,
		keep_alive=True,
		new_context_config=BrowserContextConfig(
			keep_alive=True,
			disable_security=False,
		),
	)
)

async def main():
	agent = Agent(
		task="Go to https://bot-detector.rebrowser.net/ and verify that all the bot checks are passed.",
		llm=llm,
		browser=browser,
	)
	await agent.run()
	# ... more tasks ...

if __name__ == '__main__':
	asyncio.run(main())
View full example

Using Cdp
Connect to a running Chrome instance using the Chrome DevTools Protocol (CDP) for automation.

import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig

load_dotenv()

browser = Browser(
	config=BrowserConfig(
		headless=False,
		cdp_url='http://localhost:9222',
	)
)
controller = Controller()

async def main():
	task = 'In docs.google.com write my Papa a quick thank you for everything letter'
	model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()
	await browser.close()

if __name__ == '__main__':
	asyncio.run(main())
View full example

Custom Functions
Action Filters
Limit the availability of custom actions to specific domains or pages based on URL filters.

import asyncio
from playwright.async_api import Page
from browser_use.agent.service import Agent, Browser, BrowserContext, Controller

# Initialize controller and registry
controller = Controller()
registry = controller.registry

# Action will only be available to Agent on Google domains because of the domain filter
@registry.action(description='Trigger disco mode', domains=['google.com', '*.google.com'])
async def disco_mode(browser: BrowserContext):
    page = await browser.get_current_page()
    await page.evaluate("""() => {
        document.styleSheets[0].insertRule('@keyframes wiggle { 0% { transform: rotate(0deg); } 50% { transform: rotate(10deg); } 100% { transform: rotate(0deg); } }');

        document.querySelectorAll("*").forEach(element => {
            element.style.animation = "wiggle 0.5s infinite";
        });
    }""")

# Create a custom page filter function that determines if the action should be available
def is_login_page(page: Page) -> bool:
    return 'login' in page.url.lower() or 'signin' in page.url.lower()

# Use the page filter to limit the action to only be available on login pages
@registry.action(description='Use the force, luke', page_filter=is_login_page)
async def use_the_force(browser: BrowserContext):
    # This will only ever run on pages that matched the filter
    page = await browser.get_current_page()
    assert is_login_page(page)

    await page.evaluate("""() => { document.querySelector('body').innerHTML = 'These are not the droids you are looking for';}""")

async def main():
    browser = Browser()
    agent = Agent(
        task="""
            Go to apple.com and trigger disco mode (if don't know how to do that, then just move on).
            Then go to google.com and trigger disco mode.
            After that, go to the Google login page and Use the force, luke.
        """,
        llm=ChatOpenAI(model='gpt-4o'),
        browser=browser,
        controller=controller,
    )

    await agent.run(max_steps=10)
    await browser.close()
View full example

Advanced Search
Implement a custom web search action using an external API (e.g., AskTessa) and process its results.

from pydantic import BaseModel
from browser_use import ActionResult, Agent, Controller
import httpx

class Person(BaseModel):
    name: str
    email: str | None = None

class PersonList(BaseModel):
    people: list[Person]

controller = Controller(exclude_actions=['search_google'], output_model=PersonList)
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

@controller.registry.action('Search the web for a specific query')
async def search_web(query: str):
    keys_to_use = ['url', 'title', 'content', 'author', 'score']
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'https://asktessa.ai/api/search',
            headers=headers,
            json={'query': query}
        )

    final_results = [
        {key: source[key] for key in keys_to_use if key in source}
        for source in response.json()['sources']
        if source['score'] >= 0.8
    ]
    result_text = json.dumps(final_results, indent=4)
    return ActionResult(extracted_content=result_text, include_in_memory=True)

names = [
    'Ruedi Aebersold',
    'Bernd Bodenmiller',
    # ... more names ...
]

async def main():
    task = 'use search_web with "find email address of the following ETH professor:" for each of the following persons in a list of actions. Finally return the list with name and email if provided'
    task += '\n' + '\n'.join(names)
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, controller=controller, max_actions_per_step=20)

    history = await agent.run()

    result = history.final_result()
    if result:
        parsed: PersonList = PersonList.model_validate_json(result)

        for person in parsed.people:
            print(f'{person.name} - {person.email}')
View full example

Clipboard
Define custom actions to copy text to and paste text from the system clipboard.

import pyperclip
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult

controller = Controller()

@controller.registry.action('Copy text to clipboard')
def copy_to_clipboard(text: str):
    pyperclip.copy(text)
    return ActionResult(extracted_content=text)

@controller.registry.action('Paste text from clipboard')
async def paste_from_clipboard(browser: BrowserContext):
    text = pyperclip.paste()
    # send text to browser
    page = await browser.get_current_page()
    await page.keyboard.type(text)
    return ActionResult(extracted_content=text)

async def main():
    task = 'Copy the text "Hello, world!" to the clipboard, then go to google.com and paste the text'
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model='gpt-4o'),
        controller=controller,
        browser=browser,
    )
    await agent.run()
View full example

Custom Hooks Before After Step
Record browser activity and agent state at each step using custom hook functions that interact with an external API.

import asyncio
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pyobjtojson import obj_to_json
from browser_use import Agent

async def record_activity(agent_obj):
    print('--- ON_STEP_START HOOK ---')
    website_html: str = await agent_obj.browser_context.get_page_html()
    website_screenshot: str = await agent_obj.browser_context.take_screenshot()

    # Collect data from agent history
    if hasattr(agent_obj, 'state'):
        history = agent_obj.state.history
    else:
        history = None

    model_thoughts = obj_to_json(obj=history.model_thoughts(), check_circular=False)
    # ... more data collection ...

    model_step_summary = {
        'website_html': website_html,
        'website_screenshot': website_screenshot,
        'url': urls_json_last_elem,
        'model_thoughts': model_thoughts_last_elem,
        'model_outputs': model_outputs_json_last_elem,
        'model_actions': model_actions_json_last_elem,
        'extracted_content': extracted_content_json_last_elem,
    }

    # Send data to API
    send_agent_history_step(data=model_step_summary)

agent = Agent(
    task='Compare the price of gpt-4o and DeepSeek-V3',
    llm=ChatOpenAI(model='gpt-4o'),
)

async def run_agent():
    try:
        await agent.run(on_step_start=record_activity, max_steps=30)
    except Exception as e:
        print(e)

asyncio.run(run_agent())
View full example

File Upload
Create custom actions to upload local files to a webpage and read file content within the agent’s workflow.

import os
from pathlib import Path
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

browser = Browser(
    config=BrowserConfig(
        headless=False,
    )
)
controller = Controller()

@controller.action('Upload file to interactive element with file path ')
async def upload_file(index: int, path: str, browser: BrowserContext, available_file_paths: list[str]):
    if path not in available_file_paths:
        return ActionResult(error=f'File path {path} is not available')

    if not os.path.exists(path):
        return ActionResult(error=f'File {path} does not exist')

    dom_el = await browser.get_dom_element_by_index(index)
    file_upload_dom_el = dom_el.get_file_upload_element()

    if file_upload_dom_el is None:
        return ActionResult(error=f'No file upload element found at index {index}')

    file_upload_el = await browser.get_locate_element(file_upload_dom_el)

    try:
        await file_upload_el.set_input_files(path)
        return ActionResult(extracted_content=f'Successfully uploaded file to index {index}', include_in_memory=True)
    except Exception as e:
        return ActionResult(error=f'Failed to upload file to index {index}: {str(e)}')

@controller.action('Read the file content of a file given a path')
async def read_file(path: str, available_file_paths: list[str]):
    if path not in available_file_paths:
        return ActionResult(error=f'File path {path} is not available')

    async with await anyio.open_file(path, 'r') as f:
        content = await f.read()
    return ActionResult(extracted_content=f'File content: {content}', include_in_memory=True)

# Create test files for upload
available_file_paths = [
    str(Path.cwd() / 'tmp.txt'),
    str(Path.cwd() / 'tmp.pdf'),
    str(Path.cwd() / 'tmp.csv')
]

async def main():
    agent = Agent(
        task='Go to website and upload files to fields',
        llm=ChatOpenAI(model='gpt-4o'),
        controller=controller,
        browser=browser,
        available_file_paths=available_file_paths,
    )
    await agent.run()
View full example

Hover Element
Implement a custom action to simulate hovering over a web element, specified by index, XPath, or CSS selector.

from pydantic import BaseModel
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext

class HoverAction(BaseModel):
    index: int | None = None
    xpath: str | None = None
    selector: str | None = None

controller = Controller()

@controller.registry.action(
    'Hover over an element',
    param_model=HoverAction,
)
async def hover_element(params: HoverAction, browser: BrowserContext):
    """
    Hovers over the element specified by its index from the cached selector map or by XPath.
    """
    if params.xpath:
        # Use XPath to locate the element
        element_handle = await browser.get_locate_element_by_xpath(params.xpath)
        if element_handle is None:
            raise Exception(f'Failed to locate element with XPath {params.xpath}')
    elif params.selector:
        # Use CSS selector to locate the element
        element_handle = await browser.get_locate_element_by_css_selector(params.selector)
        if element_handle is None:
            raise Exception(f'Failed to locate element with CSS Selector {params.selector}')
    elif params.index is not None:
        # Use index to locate the element
        element_node = state.selector_map[params.index]
        element_handle = await browser.get_locate_element(element_node)
        if element_handle is None:
            raise Exception(f'Failed to locate element with index {params.index}')
    else:
        raise Exception('Either index or xpath must be provided')

    try:
        await element_handle.hover()
        return ActionResult(extracted_content=f'🖱️ Hovered over element', include_in_memory=True)
    except Exception as e:
        raise Exception(f'Failed to hover over element: {str(e)}')

async def main():
    task = 'Open webpage and hover the element with the css selector #hoverdivpara'
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model='gpt-4o'),
        controller=controller,
    )
    await agent.run()
View full example

Notification
Define a custom action to send a notification (e.g., an email) when a task is completed.

import yagmail
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult

controller = Controller()

@controller.registry.action('Done with task ')
async def done(text: str):
    # To send emails use
    # STEP 1: go to https://support.google.com/accounts/answer/185833
    # STEP 2: Create an app password (you can't use here your normal gmail password)
    # STEP 3: Use the app password in the code below for the password
    yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')
    yag.send(
        to='recipient@example.com',
        subject='Test Email',
        contents=f'result\n: {text}',
    )

    return ActionResult(is_done=True, extracted_content='Email sent!')

async def main():
    task = 'go to brower-use.com and then done'
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model='gpt-4o'),
        controller=controller
    )
    await agent.run()
View full example

Onepassword 2fa
Integrate 1Password to fetch 2FA codes for logging into services like Google.

import asyncio
from onepassword.client import Client
from browser_use import ActionResult, Agent, Controller

controller = Controller()

@controller.registry.action('Get 2FA code from 1Password for Google Account', domains=['*.google.com', 'google.com'])
async def get_1password_2fa() -> ActionResult:
    """
    Custom action to retrieve 2FA/MFA code from 1Password using onepassword.client SDK.
    """
    client = await Client.authenticate(
        auth=OP_SERVICE_ACCOUNT_TOKEN,
        integration_name='Browser-Use',
        integration_version='v1.0.0',
    )

    mfa_code = await client.secrets.resolve(f'op://Private/{OP_ITEM_ID}/One-time passcode')

    return ActionResult(extracted_content=mfa_code)

async def main():
    task = 'Go to account.google.com, enter username and password, then if prompted for 2FA code, get 2FA code from 1Password for and enter it'

    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, controller=controller)

    result = await agent.run()
View full example

Save To File Hugging Face
Create a custom action to save structured data (e.g., Hugging Face model information) to a local file.

from pydantic import BaseModel
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult

controller = Controller()

class Model(BaseModel):
	title: str
	url: str
	likes: int
	license: str

class Models(BaseModel):
	models: list[Model]

@controller.action('Save models', param_model=Models)
def save_models(params: Models):
	with open('models.txt', 'a') as f:
		for model in params.models:
			f.write(f'{model.title} ({model.url}): {model.likes} likes, {model.license}\n')

async def main():
	task = 'Look up models with a license of cc-by-sa-4.0 and sort by most likes on Hugging face, save top 5 to file.'

	agent = Agent(
		task=task,
		llm=ChatOpenAI(model='gpt-4o'),
		controller=controller
	)

	await agent.run()
View full example

Validate Output
Enforce a specific output structure for custom actions using Pydantic models and validate the agent’s adherence to it.

from pydantic import BaseModel
from browser_use import Agent, Controller, ActionResult

controller = Controller()


class DoneResult(BaseModel):
	title: str
	comments: str
	hours_since_start: int


# we overwrite done() in this example to demonstrate the validator
@controller.registry.action('Done with task', param_model=DoneResult)
async def done(params: DoneResult):
	result = ActionResult(is_done=True, extracted_content=params.model_dump_json())
	print(result)
	# NOTE: this is clearly wrong - to demonstrate the validator
	return 'blablabla'


async def main():
	task = 'Go to hackernews hn and give me the top 1 post'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller, validate_output=True)
	# NOTE: this should fail to demonstrate the validator
	await agent.run(max_steps=5)
View full example

Features
Click Fallback Options
Demonstrates robust element clicking by trying various methods (XPath, CSS selector, text) on a test page with custom select dropdowns.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller

controller = Controller()

async def main():
    # Example tasks showing different ways to click elements
    xpath_task = 'Open http://localhost:8000/, click element with the xpath "/html/body/div/div[1]" and then click on Oranges'
    css_selector_task = 'Open http://localhost:8000/, click element with the selector div.select-display and then click on apples'
    text_task = 'Open http://localhost:8000/, click the third element with the text "Select a fruit" and then click on Apples'
    select_task = 'Open http://localhost:8000/, choose the car BMW'
    button_task = 'Open http://localhost:8000/, click on the button'

    llm = ChatOpenAI(model='gpt-4o')

    # Run different agent tasks demonstrating various click methods
    for task in [xpath_task, css_selector_task, text_task, select_task, button_task]:
        agent = Agent(
            task=task,
            llm=llm,
            controller=controller,
        )
        await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Cross Origin Iframes
Interact with elements inside cross-origin iframes.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig

browser = Browser(
    config=BrowserConfig(
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    )
)
controller = Controller()

async def main():
    agent = Agent(
        task='Click "Go cross-site (simple page)" button on https://csreis.github.io/tests/cross-site-iframe.html then tell me the text within',
        llm=ChatOpenAI(model='gpt-4o', temperature=0.0),
        controller=controller,
        browser=browser,
    )

    await agent.run()
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Custom Output
Define a Pydantic model to structure the agent’s final output, for example, extracting a list of Hacker News posts.

from pydantic import BaseModel
from browser_use import Agent, Controller

class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int

class Posts(BaseModel):
	posts: list[Post]

controller = Controller(output_model=Posts)

async def main():
	task = 'Go to hackernews show hn and give me the first 5 posts'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller)

	history = await agent.run()

	result = history.final_result()
	if result:
		parsed: Posts = Posts.model_validate_json(result)

		for post in parsed.posts:
			print(f'Title:            {post.post_title}')
			print(f'URL:              {post.post_url}')
			print(f'Comments:         {post.num_comments}')
			print(f'Hours since post: {post.hours_since_post}')
View full example

Custom System Prompt
Extend or override the default system prompt to give the agent specific instructions or context.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

extend_system_message = (
    'REMEMBER the most important RULE: ALWAYS open first a new tab and go first to url wikipedia.com no matter the task!!!'
)

# or use override_system_message to completely override the system prompt

async def main():
    task = "do google search to find images of Elon Musk's wife"
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, extend_system_message=extend_system_message)

    print(
        json.dumps(
            agent.message_manager.system_prompt.model_dump(exclude_unset=True),
            indent=4,
        )
    )

    await agent.run()
View full example

Custom User Agent
Set a custom user agent string for the browser context.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

browser = Browser(
    config=BrowserConfig(
        # browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    )
)

browser_context = BrowserContext(config=BrowserContextConfig(user_agent='foobarfoo'), browser=browser)

agent = Agent(
    task='go to https://whatismyuseragent.com and find the current user agent string',
    llm=ChatOpenAI(model='gpt-4o'),
    browser_context=browser_context,
    use_vision=True,
)

async def main():
    await agent.run()
    await browser_context.close()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Download File
Download a file from a webpage to a specified local directory.

import os
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig

browser = Browser(
    config=BrowserConfig(
        new_context_config=BrowserContextConfig(save_downloads_path=os.path.join(os.path.expanduser('~'), 'downloads'))
    )
)

async def run_download():
    agent = Agent(
        task='Go to "https://file-examples.com/" and download the smallest doc file.',
        llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp'),
        max_actions_per_step=8,
        use_vision=True,
        browser=browser,
    )
    await agent.run(max_steps=25)
    await browser.close()
View full example

Drag Drop
Perform drag-and-drop operations on web elements, such as reordering items in a list or drawing on a canvas.

import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

task = """
Navigate to: https://sortablejs.github.io/Sortable/.
Then scroll down to the first examplw with title "Simple list example".
Drag the element with name "item 1" to below the element with name "item 3".
"""

async def run_search():
    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp'),
        max_actions_per_step=1,
        use_vision=True,
    )

    await agent.run(max_steps=25)

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Follow Up Tasks
Chain multiple tasks together, where a new task can be added and run after the previous one completes.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig, Controller

browser = Browser(
    config=BrowserConfig(
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        new_context_config=BrowserContextConfig(
            keep_alive=True,
        ),
    ),
)
controller = Controller()

task = 'Find the founders of browser-use and draft them a short personalized message'
agent = Agent(task=task, llm=ChatOpenAI(model='gpt-4o'), controller=controller, browser=browser)

async def main():
    await agent.run()

    # new_task = input('Type in a new task: ')
    new_task = 'Find an image of the founders'

    agent.add_new_task(new_task)

    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Initial Actions
Specify a sequence of actions for the agent to perform at the very beginning of its run, before processing the main task.

from langchain_openai import ChatOpenAI
from browser_use import Agent

initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
]
agent = Agent(
	task='What theories are displayed on the page?',
	initial_actions=initial_actions,
	llm=ChatOpenAI(model='gpt-4o'),
)

async def main():
	await agent.run(max_steps=10)

if __name__ == '__main__':
	import asyncio
	asyncio.run(main())
View full example

Multi Tab Handling
Manage multiple browser tabs, such as opening several pages and navigating between them.

from langchain_openai import ChatOpenAI
from browser_use import Agent

# video: https://preview.screen.studio/share/clenCmS6
llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='open 3 tabs with elon musk, trump, and steve jobs, then go back to the first and stop',
	llm=llm,
)

async def main():
	await agent.run()

asyncio.run(main())
View full example

Multiple Agents Same Browser
Run multiple agents concurrently or sequentially within the same browser instance and context, allowing them to share session state.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser

async def main():
    # Persist the browser state across agents
    browser = Browser()
    async with await browser.new_context() as context:
        model = ChatOpenAI(model='gpt-4o')
        current_agent = None

        async def get_input():
            return await asyncio.get_event_loop().run_in_executor(
                None, lambda: input('Enter task (p: pause current agent, r: resume, b: break): ')
            )

        while True:
            task = await get_input()

            if task.lower() == 'p':
                # Pause the current agent if one exists
                if current_agent:
                    current_agent.pause()
                continue
            elif task.lower() == 'r':
                # Resume the current agent if one exists
                if current_agent:
                    current_agent.resume()
                continue
            elif task.lower() == 'b':
                # Break the current agent's execution if one exists
                if current_agent:
                    current_agent.stop()
                    current_agent = None
                continue

            # If there's a current agent running, pause it before starting new one
            if current_agent:
                current_agent.pause()

            # Create and run new agent with the task
            current_agent = Agent(
                task=task,
                llm=model,
                browser_context=context,
            )

            # Run the agent asynchronously without blocking
            asyncio.create_task(current_agent.run())
View full example

Outsource State
Persist and load agent state (excluding history) to/from a file, allowing for resumption or transfer of agent progress.

import anyio
from browser_use.agent.views import AgentState
from browser_use import Agent

# Create initial agent state
agent_state = AgentState()

# Use agent with the state
agent = Agent(
    task=task,
    llm=ChatOpenAI(model='gpt-4o'),
    browser=browser,
    browser_context=browser_context,
    injected_agent_state=agent_state,
    page_extraction_llm=ChatOpenAI(model='gpt-4o-mini'),
)

done, valid = await agent.take_step()

# Clear history before saving state
agent_state.history.history = []

# Save state to file
async with await anyio.open_file('agent_state.json', 'w') as f:
    serialized = agent_state.model_dump_json(exclude={'history'})
    await f.write(serialized)

# Load state back from file
async with await anyio.open_file('agent_state.json', 'r') as f:
    loaded_json = await f.read()
    agent_state = AgentState.model_validate_json(loaded_json)
View full example

Parallel Agents
Execute multiple agents simultaneously, each performing a different task in its own browser context.

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig

browser = Browser(
    config=BrowserConfig(
        disable_security=True,
        headless=False,
        new_context_config=BrowserContextConfig(save_recording_path='./tmp/recordings'),
    )
)
llm = ChatOpenAI(model='gpt-4o')

async def main():
    agents = [
        Agent(task=task, llm=llm, browser=browser)
        for task in [
            'Search Google for weather in Tokyo',
            'Check Reddit front page title',
            'Look up Bitcoin price on Coinbase',
            'Find NASA image of the day',
            # 'Check top story on CNN',
            # 'Search latest SpaceX launch date',
            # ...
        ]
    ]

    await asyncio.gather(*[agent.run() for agent in agents])

    # Run another agent after parallel agents complete
    agentX = Agent(
        task='Go to apple.com and return the title of the page',
        llm=llm,
        browser=browser,
    )
    await agentX.run()

    await browser.close()
View full example

Pause Agent
Control an agent’s execution by pausing, resuming, or stopping it through an external interface or thread.

import threading
from langchain_openai import ChatOpenAI
from browser_use import Agent

class AgentController:
    def __init__(self):
        llm = ChatOpenAI(model='gpt-4o')
        self.agent = Agent(
            task='open in one action https://www.google.com, https://www.wikipedia.org, https://www.youtube.com, https://www.github.com, https://amazon.com',
            llm=llm,
        )
        self.running = False

    async def run_agent(self):
        """Run the agent"""
        self.running = True
        await self.agent.run()

    def start(self):
        """Start the agent in a separate thread"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.run_agent())

    def pause(self):
        """Pause the agent"""
        self.agent.pause()

    def resume(self):
        """Resume the agent"""
        self.agent.resume()

    def stop(self):
        """Stop the agent"""
        self.agent.stop()
        self.running = False

async def main():
    controller = AgentController()
    agent_thread = None

    # ... menu code ...

    if choice == '1' and not agent_thread:
        print('Starting agent...')
        agent_thread = threading.Thread(target=controller.start)
        agent_thread.start()

    elif choice == '2':
        print('Pausing agent...')
        controller.pause()

    elif choice == '3':
        print('Resuming agent...')
        controller.resume()

    elif choice == '4':
        print('Stopping agent...')
        controller.stop()
        if agent_thread:
            agent_thread.join()
            agent_thread = None
View full example

Planner
Utilize a separate LLM as a planner to break down a complex task into smaller steps for the agent.

from langchain_openai import ChatOpenAI
from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)
planner_llm = ChatOpenAI(
	model='o3-mini',
)
task = 'your task'

agent = Agent(task=task, llm=llm, planner_llm=planner_llm, use_vision_for_planner=False, planner_interval=1)

async def main():
	await agent.run()

if __name__ == '__main__':
	asyncio.run(main())
View full example

Playwright Script Generation
Automatically generate a Playwright script based on the agent’s actions, which can then be executed independently.

from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

# Define the task for the agent
TASK_DESCRIPTION = """
1. Go to amazon.com
2. Search for 'i7 14700k'
4. If there is an 'Add to Cart' button, open the product page and then click add to cart.
5. the open the shopping cart page /cart button/ go to cart button.
6. Scroll down to the bottom of the cart page.
7. Scroll up to the top of the cart page.
8. Finish the task.
"""

# Define the path where the Playwright script will be saved
SCRIPT_DIR = Path('./playwright_scripts')
SCRIPT_PATH = SCRIPT_DIR / 'playwright_amazon_cart_script.py'

async def main():
    # Initialize the language model
    llm = ChatOpenAI(model='gpt-4.1', temperature=0.0)

    # Configure the browser
    browser_config = BrowserConfig(headless=False)
    browser = Browser(config=browser_config)

    # Configure the agent
    # The 'save_playwright_script_path' argument tells the agent where to save the script
    agent = Agent(
        task=TASK_DESCRIPTION,
        llm=llm,
        browser=browser,
        save_playwright_script_path=str(SCRIPT_PATH),  # Pass the path as a string
    )

    print('Running the agent to generate the Playwright script...')
    history = await agent.run()

    # ... executing the generated script ...
    if SCRIPT_PATH.exists():
        process = await asyncio.create_subprocess_exec(
            sys.executable,
            str(SCRIPT_PATH),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=Path.cwd(),  # Run from the current working directory
        )

        # ... output streaming code ...

    # Close the browser used by the agent
    if browser:
        await browser.close()
View full example

Restrict Urls
Confine the agent’s browsing activity to a predefined list of allowed domains.

from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)
task = "go to google.com and search for openai.com and click on the first link then extract content and scroll down"

allowed_domains = ['google.com']

browser = Browser(
	config=BrowserConfig(
		browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
		new_context_config=BrowserContextConfig(
			allowed_domains=allowed_domains,
		),
	),
)

agent = Agent(
	task=task,
	llm=llm,
	browser=browser,
)

async def main():
	await agent.run(max_steps=25)
	# ...
View full example

Result Processing
Access and process various components of the agent’s execution history, such as final results, errors, model actions, and thoughts.

from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.agent.views import AgentHistoryList

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
    task="go to google.com and type 'OpenAI' click search and give me the first url",
    llm=llm,
    browser_context=browser_context,
)
history: AgentHistoryList = await agent.run(max_steps=3)

print('Final Result:')
pprint(history.final_result(), indent=4)

print('\nErrors:')
pprint(history.errors(), indent=4)

# e.g. xPaths the model clicked on
print('\nModel Outputs:')
pprint(history.model_actions(), indent=4)

print('\nThoughts:')
pprint(history.model_thoughts(), indent=4)
View full example

Save Trace
Record a Playwright trace of the agent’s browser interactions for debugging and visualization.

from langchain_openai import ChatOpenAI
from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContextConfig

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)

async def main():
    browser = Browser()

    async with await browser.new_context(config=BrowserContextConfig(trace_path='./tmp/traces/')) as context:
        agent = Agent(
            task='Go to hackernews, then go to apple.com and return all titles of open tabs',
            llm=llm,
            browser_context=context,
        )
        await agent.run()

    await browser.close()
View full example

Sensitive Data
Handle sensitive information (e.g., login credentials) by providing them to the agent in a way that they are used but not directly exposed in logs or prompts.

from langchain_openai import ChatOpenAI
from browser_use import Agent

llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.0,
)
# the model will see x_name and x_password, but never the actual values.
sensitive_data = {'x_name': 'my_x_name', 'x_password': 'my_x_password'}
task = 'go to x.com and login with x_name and x_password then find interesting posts and like them'

agent = Agent(task=task, llm=llm, sensitive_data=sensitive_data)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Small Model For Extraction
Use a smaller, potentially faster or cheaper, LLM for page content extraction while a more capable LLM handles main task processing.

from langchain_openai import ChatOpenAI
from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o', temperature=0.0)
small_llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.0)
task = 'Find the founders of browser-use in ycombinator, extract all links and open the links one by one'
agent = Agent(task=task, llm=llm, page_extraction_llm=small_llm)

async def main():
	await agent.run()

if __name__ == '__main__':
	asyncio.run(main())
View full example

Task With Memory
Enable long-term memory for the agent to retain information across multiple steps while performing a complex, multi-page task like summarizing documentation.

# Define a list of links to process
links = [
    'https://docs.mem0.ai/components/llms/models/litellm',
    'https://docs.mem0.ai/components/llms/models/mistral_AI',
    # ... more links ...
]

class Link(BaseModel):
    url: str
    title: str
    summary: str

class Links(BaseModel):
    links: list[Link]

initial_actions = [
    {'open_tab': {'url': 'https://docs.mem0.ai/'}},
]
controller = Controller(output_model=Links)
task_description = f"""
Visit all the links provided in {links} and summarize the content of the page with url and title.
There are {len(links)} links to visit. Make sure to visit all the links.
Return a json with the following format: [].
"""

async def main(max_steps=500):
    config = BrowserConfig(headless=True)
    browser = Browser(config=config)

    agent = Agent(
        task=task_description,
        llm=ChatOpenAI(model='gpt-4o-mini'),
        controller=controller,
        initial_actions=initial_actions,
        enable_memory=True,
        browser=browser,
    )
    history = await agent.run(max_steps=max_steps)
    result = history.final_result()
    parsed_result = []
    if result:
        parsed: Links = Links.model_validate_json(result)
        # ... process and save results ...
View full example

Validate Output
Enforce a specific output structure for custom actions using Pydantic models and validate the agent’s adherence to it.

from pydantic import BaseModel
from browser_use import Agent, Controller, ActionResult

controller = Controller()


class DoneResult(BaseModel):
	title: str
	comments: str
	hours_since_start: int


# we overwrite done() in this example to demonstrate the validator
@controller.registry.action('Done with task', param_model=DoneResult)
async def done(params: DoneResult):
	result = ActionResult(is_done=True, extracted_content=params.model_dump_json())
	print(result)
	# NOTE: this is clearly wrong - to demonstrate the validator
	return 'blablabla'


async def main():
	task = 'Go to hackernews hn and give me the top 1 post'
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(task=task, llm=model, controller=controller, validate_output=True)
	# NOTE: this should fail to demonstrate the validator
	await agent.run(max_steps=5)
View full example

Integrations
Discord Api
Create a Discord bot that uses Browser Use to perform tasks based on user messages.

from discord.ext import commands
from langchain_core.language_models.chat_models import BaseChatModel
from browser_use import BrowserConfig
from browser_use.agent.service import Agent, Browser

class DiscordBot(commands.Bot):
    def __init__(
        self,
        llm: BaseChatModel,
        prefix: str = '$bu',
        ack: bool = False,
        browser_config: BrowserConfig = BrowserConfig(headless=True),
    ):
        self.llm = llm
        self.prefix = prefix.strip()
        self.ack = ack
        self.browser_config = browser_config

        # Define intents.
        intents = discord.Intents.default()
        intents.message_content = True  # Enable message content intent
        intents.members = True  # Enable members intent for user info

        # Initialize the bot with a command prefix and intents.
        super().__init__(command_prefix='!', intents=intents)

    async def on_message(self, message):
        """Called when a message is received."""
        try:
            if message.author == self.user:  # Ignore the bot's messages
                return
            if message.content.strip().startswith(f'{self.prefix} '):
                if self.ack:
                    await message.reply('Starting browser use task...', mention_author=True)

                try:
                    agent_message = await self.run_agent(message.content.replace(f'{self.prefix} ', '').strip())
                    await message.channel.send(content=f'{agent_message}', reference=message, mention_author=True)
                except Exception as e:
                    await message.channel.send(
                        content=f'Error during task execution: {str(e)}',
                        reference=message,
                        mention_author=True,
                    )
        except Exception as e:
            print(f'Error in message handling: {e}')

    async def run_agent(self, task: str) -> str:
        try:
            browser = Browser(config=self.browser_config)
            agent = Agent(task=(task), llm=self.llm, browser=browser)
            result = await agent.run()

            agent_message = None
            if result.is_done():
                agent_message = result.history[-1].result[0].extracted_content

            if agent_message is None:
                agent_message = 'Oops! Something went wrong while running Browser-Use.'

            return agent_message
        except Exception as e:
            raise Exception(f'Browser-use task failed: {str(e)}')
View full example

Discord Example
Run a Discord bot that listens for commands and executes browser automation tasks using an LLM.

from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import BrowserConfig
from examples.integrations.discord.discord_api import DiscordBot

# Load credentials from environment variables
bot_token = os.getenv('DISCORD_BOT_TOKEN')
api_key = os.getenv('GEMINI_API_KEY')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

bot = DiscordBot(
    llm=llm,  # required; instance of BaseChatModel
    prefix='$bu',  # optional; prefix of messages to trigger browser-use
    ack=True,  # optional; whether to acknowledge task receipt with a message
    browser_config=BrowserConfig(
        headless=False
    ),  # optional; useful for changing headless mode or other browser configs
)

bot.run(
    token=bot_token,  # required; Discord bot token
)
View full example

Slack Api
Develop a Slack bot integrated with FastAPI to handle events and execute browser tasks.

from fastapi import FastAPI, Request, Depends
from slack_sdk.web.async_client import AsyncWebClient
from langchain_core.language_models.chat_models import BaseChatModel
from browser_use import BrowserConfig
from browser_use.agent.service import Agent, Browser

class SlackBot:
    def __init__(
        self,
        llm: BaseChatModel,
        bot_token: str,
        signing_secret: str,
        ack: bool = False,
        browser_config: BrowserConfig = BrowserConfig(headless=True),
    ):
        self.llm = llm
        self.ack = ack
        self.browser_config = browser_config
        self.client = AsyncWebClient(token=bot_token)
        self.signature_verifier = SignatureVerifier(signing_secret)
        self.processed_events = set()

    async def handle_event(self, event, event_id):
        # ... event processing ...
        if text and text.startswith('$bu '):
            task = text[len('$bu ') :].strip()
            if self.ack:
                await self.send_message(
                    event['channel'], f'<@{user_id}> Starting browser use task...', thread_ts=event.get('ts')
                )

            try:
                agent_message = await self.run_agent(task)
                await self.send_message(event['channel'], f'<@{user_id}> {agent_message}', thread_ts=event.get('ts'))
            except Exception as e:
                await self.send_message(event['channel'], f'Error during task execution: {str(e)}', thread_ts=event.get('ts'))

    async def run_agent(self, task: str) -> str:
        try:
            browser = Browser(config=self.browser_config)
            agent = Agent(task=task, llm=self.llm, browser=browser)
            result = await agent.run()

            agent_message = None
            if result.is_done():
                agent_message = result.history[-1].result[0].extracted_content

            if agent_message is None:
                agent_message = 'Oops! Something went wrong while running Browser-Use.'

            return agent_message
        except Exception as e:
            return f'Error during task execution: {str(e)}'

# FastAPI endpoint for handling Slack events
@app.post('/slack/events')
async def slack_events(request: Request, slack_bot: Annotated[SlackBot, Depends()]):
    # ... request verification ...
    event_data = await request.json()
    if 'event' in event_data:
        await slack_bot.handle_event(event_data.get('event'), event_data.get('event_id'))
    return {}
View full example

Slack Example
Run a Slack bot that uses Browser Use to perform tasks triggered by Slack messages.

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import BrowserConfig
from examples.integrations.slack.slack_api import SlackBot, app

load_dotenv()

# Load credentials from environment variables
bot_token = os.getenv('SLACK_BOT_TOKEN')
signing_secret = os.getenv('SLACK_SIGNING_SECRET')
api_key = os.getenv('GEMINI_API_KEY')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

slack_bot = SlackBot(
    llm=llm,  # required; instance of BaseChatModel
    bot_token=bot_token,  # required; Slack bot token
    signing_secret=signing_secret,  # required; Slack signing secret
    ack=True,  # optional; whether to acknowledge task receipt with a message
    browser_config=BrowserConfig(
        headless=True
    ),  # optional; useful for changing headless mode or other browser configs
)

app.dependency_overrides[SlackBot] = lambda: slack_bot

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('integrations.slack.slack_api:app', host='0.0.0.0', port=3000)
Models
Azure Openai
Use an Azure OpenAI model (e.g., GPT-4o) as the LLM for the agent.

from langchain_openai import AzureChatOpenAI
from browser_use import Agent

# Retrieve Azure-specific environment variables
azure_openai_api_key = os.getenv('AZURE_OPENAI_KEY')
azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

# Initialize the Azure OpenAI client
llm = AzureChatOpenAI(
    model_name='gpt-4o',
    openai_api_key=azure_openai_api_key,
    azure_endpoint=azure_openai_endpoint,
    deployment_name='gpt-4o',
    api_version='2024-08-01-preview',
)

agent = Agent(
    task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
    llm=llm,
    enable_memory=True,
)

async def main():
    await agent.run(max_steps=10)

asyncio.run(main())
View full example

Bedrock Claude
Utilize an AWS Bedrock model (e.g., Claude Sonnet) as the LLM for the agent to perform web automation tasks.

import boto3
from botocore.config import Config
from langchain_aws import ChatBedrockConverse
from browser_use import Agent

def get_llm():
	config = Config(retries={'max_attempts': 10, 'mode': 'adaptive'})
	bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1', config=config)

	return ChatBedrockConverse(
		model_id='us.anthropic.claude-3-5-sonnet-20241022-v2:0',
		temperature=0.0,
		max_tokens=None,
		client=bedrock_client,
	)

# Define the task for the agent
task = (
	"Visit cnn.com, navigate to the 'World News' section, and identify the latest headline. "
	'Open the first article and summarize its content in 3-4 sentences.'
	# ... task continues ...
)

llm = get_llm()

agent = Agent(
	task=args.query,
	llm=llm,
	controller=Controller(),
	browser=browser,
	validate_output=True,
)

async def main():
	await agent.run(max_steps=30)
	await browser.close()

asyncio.run(main())
View full example

Claude 3 7 Sonnet
Employ Anthropic’s Claude 3.7 Sonnet model as the LLM for the agent.

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from browser_use import Agent

# Load environment variables from .env file
load_dotenv()

llm = ChatAnthropic(model_name='claude-3-7-sonnet-20250219', temperature=0.0, timeout=30, stop=None)

agent = Agent(
	task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
	llm=llm,
)

async def main():
	await agent.run(max_steps=10)

asyncio.run(main())
View full example

Deepseek
Use a DeepSeek model (e.g., deepseek-chat) via its API as the LLM for the agent.

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY', '')

async def run_search():
    agent = Agent(
        task=(
            '1. Go to https://www.reddit.com/r/LocalLLaMA '
            "2. Search for 'browser use' in the search bar"
            '3. Click on first result'
            '4. Return the first comment'
        ),
        llm=ChatDeepSeek(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-chat',
            api_key=SecretStr(api_key),
        ),
        use_vision=False,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

DeepSeek R1
Utilize the DeepSeek Reasoner (R1) model for complex web automation tasks.

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()

api_key = os.getenv('DEEPSEEK_API_KEY', '')

async def run_search():
    agent = Agent(
        task=('go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result'),
        llm=ChatDeepSeek(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-reasoner',
            api_key=SecretStr(api_key),
        ),
        use_vision=False,
        max_failures=2,
        max_actions_per_step=1,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Gemini
Leverage a Google Gemini model (e.g., gemini-2.0-flash-exp) as the LLM for the agent.

import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent, BrowserConfig
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContextConfig

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

browser = Browser(
    config=BrowserConfig(
        new_context_config=BrowserContextConfig(
            viewport_expansion=0,
        )
    )
)

async def run_search():
    agent = Agent(
        task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
        llm=llm,
        max_actions_per_step=4,
        browser=browser,
    )

    await agent.run(max_steps=25)

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Gpt 4o
Use OpenAI’s GPT-4o model as the LLM for the agent.

from langchain_openai import ChatOpenAI
from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
	llm=llm,
)


async def main():
	await agent.run(max_steps=10)


asyncio.run(main())
View full example

Grok
Employ a Grok model via its API as the LLM for the agent.

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()

api_key = os.getenv('GROK_API_KEY', '')

async def run_search():
    agent = Agent(
        task=(
            'Go to amazon.com, search for wireless headphones, filter by highest rating, and return the title and price of the first product'
        ),
        llm=ChatOpenAI(
            base_url='https://api.x.ai/v1',
            model='grok-3-beta',
            api_key=SecretStr(api_key),
        ),
        use_vision=False,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Novita
Use a Novita.ai model (e.g., deepseek-v3) as the LLM for the agent.

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

load_dotenv()
api_key = os.getenv('NOVITA_API_KEY', '')

async def run_search():
    agent = Agent(
        task=(
            'Go to https://www.reddit.com/r/LocalLLaMA, search for "browser use" in the search bar, '
            'click on first result, and return the first comment'
        ),
        llm=ChatOpenAI(
            base_url='https://api.novita.ai/v3/openai',
            model='deepseek/deepseek-v3-0324',
            api_key=SecretStr(api_key),
        ),
        use_vision=False,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Ollama
Run an agent using a locally hosted LLM through Ollama (e.g., Qwen 2.5).

import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent

async def run_search():
    agent = Agent(
        task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
        llm=ChatOllama(
            model='qwen2.5:32b-instruct-q4_K_M',
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return result

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

Qwen
Use a Qwen model via Ollama as the LLM for the agent.

import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent

async def run_search():
    agent = Agent(
        task=(
            "1. Go to https://www.reddit.com/r/LocalLLaMA2. Search for 'browser use' in the search bar3. Click search4. Call done"
        ),
        llm=ChatOllama(
            # model='qwen2.5:32b-instruct-q4_K_M',
            # model='qwen2.5:14b',
            model='qwen2.5:latest',
            num_ctx=128000,
        ),
        max_actions_per_step=1,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_search())
View full example

UI
Command Line
Run browser automation tasks from the command line, specifying the query and LLM provider (OpenAI or Anthropic).

import argparse
import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

load_dotenv()

def get_llm(provider: str):
    if provider == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0)
    elif provider == 'openai':
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model='gpt-4o', temperature=0.0)
    else:
        raise ValueError(f'Unsupported provider: {provider}')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Automate browser tasks using an LLM agent.')
    parser.add_argument(
        '--query', type=str, help='The query to process', default='go to reddit and search for posts about browser-use'
    )
    parser.add_argument(
        '--provider',
        type=str,
        choices=['openai', 'anthropic'],
        default='openai',
        help='The model provider to use (default: openai)',
    )
    return parser.parse_args()

def initialize_agent(query: str, provider: str):
    llm = get_llm(provider)
    controller = Controller()
    browser = Browser(config=BrowserConfig())

    return Agent(
        task=query,
        llm=llm,
        controller=controller,
        browser=browser,
        use_vision=True,
        max_actions_per_step=1,
    ), browser

async def main():
    args = parse_arguments()
    agent, browser = initialize_agent(args.query, args.provider)
    await agent.run(max_steps=25)
    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
View full example

Gradio Demo
Create a Gradio web interface to input tasks and API keys for running Browser Use agents.

import asyncio
import os
import gradio as gr
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

async def run_browser_task(
    task: str,
    api_key: str,
    model: str = 'gpt-4o',
    headless: bool = True,
) -> str:
    if not api_key.strip():
        return 'Please provide an API key'

    os.environ['OPENAI_API_KEY'] = api_key

    try:
        agent = Agent(
            task=task,
            llm=ChatOpenAI(model='gpt-4o'),
        )
        result = await agent.run()
        return result
    except Exception as e:
        return f'Error: {str(e)}'

def create_ui():
    with gr.Blocks(title='Browser Use GUI') as interface:
        gr.Markdown('# Browser Use Task Automation')

        with gr.Row():
            with gr.Column():
                api_key = gr.Textbox(label='OpenAI API Key', placeholder='sk-...', type='password')
                task = gr.Textbox(
                    label='Task Description',
                    placeholder='E.g., Find flights from New York to London for next week',
                    lines=3,
                )
                model = gr.Dropdown(choices=['gpt-4', 'gpt-3.5-turbo'], label='Model', value='gpt-4')
                headless = gr.Checkbox(label='Run Headless', value=True)
                submit_btn = gr.Button('Run Task')

            with gr.Column():
                output = gr.Textbox(label='Output', lines=10, interactive=False)

        submit_btn.click(
            fn=lambda *args: asyncio.run(run_browser_task(*args)),
            inputs=[task, api_key, model, headless],
            outputs=output,
        )

    return interface

if __name__ == '__main__':
    demo = create_ui()
    demo.launch()
Streamlit Demo
Build a Streamlit web application to control a Browser Use agent, allowing users to input queries and select LLM providers.

import asyncio
import os
import streamlit as st
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller

# Load environment variables
load_dotenv()

# Function to get the LLM based on provider
def get_llm(provider: str):
    if provider == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0)
    elif provider == 'openai':
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model='gpt-4o', temperature=0.0)
    else:
        st.error(f'Unsupported provider: {provider}')
        st.stop()

# Function to initialize the agent
def initialize_agent(query: str, provider: str):
    llm = get_llm(provider)
    controller = Controller()
    browser = Browser(config=BrowserConfig())

    return Agent(
        task=query,
        llm=llm,
        controller=controller,
        browser=browser,
        use_vision=True,
        max_actions_per_step=1,
    ), browser

# Streamlit UI
st.title('Automated Browser Agent with LLMs 🤖')

query = st.text_input('Enter your query:', 'go to reddit and search for posts about browser-use')
provider = st.radio('Select LLM Provider:', ['openai', 'anthropic'], index=0)

if st.button('Run Agent'):
    st.write('Initializing agent...')
    agent, browser = initialize_agent(query, provider)

    async def run_agent():
        with st.spinner('Running automation...'):
            await agent.run(max_steps=25)
        st.success('Task completed! 🎉')

    asyncio.run(run_agent())

    st.button('Close Browser', on_click=lambda: asyncio.run(browser.close()))
View full example

Use Cases
Captcha
Attempt to solve CAPTCHAs on a demo website.

from langchain_openai import ChatOpenAI
from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
    task='go to https://captcha.com/demos/features/captcha-demo.aspx and solve the captcha',
    llm=llm,
)
await agent.run()
View full example

Check Appointment
Check for available visa appointment slots on a government website.

from pydantic import BaseModel
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller

controller = Controller()

class WebpageInfo(BaseModel):
    """Model for webpage link."""
    link: str = 'https://appointment.mfa.gr/en/reservations/aero/ireland-grcon-dub/'

@controller.action('Go to the webpage', param_model=WebpageInfo)
def go_to_webpage(webpage_info: WebpageInfo):
    """Returns the webpage link."""
    return webpage_info.link

async def main():
    task = (
        'Go to the Greece MFA webpage via the link I provided you.'
        'Check the visa appointment dates. If there is no available date in this month, check the next month.'
        'If there is no available date in both months, tell me there is no available date.'
    )

    model = ChatOpenAI(model='gpt-4o-mini')
    agent = Agent(task, model, controller=controller, use_vision=True)

    await agent.run()
View full example

Find And Apply To Jobs
Automate searching for job listings, evaluating them against a CV, and initiating applications.

from pydantic import BaseModel
from browser_use import ActionResult, Agent, Controller
from PyPDF2 import PdfReader

controller = Controller()
CV = Path.cwd() / 'cv_04_24.pdf'

class Job(BaseModel):
    title: str
    link: str
    company: str
    fit_score: float
    location: str | None = None
    salary: str | None = None

@controller.action('Save jobs to file - with a score how well it fits to my profile', param_model=Job)
def save_jobs(job: Job):
    with open('jobs.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([job.title, job.company, job.link, job.salary, job.location])

    return 'Saved job to file'

@controller.action('Read my cv for context to fill forms')
def read_cv():
    pdf = PdfReader(CV)
    text = ''
    for page in pdf.pages:
        text += page.extract_text() or ''
    return ActionResult(extracted_content=text, include_in_memory=True)

@controller.action(
    'Upload cv to element - call this function to upload if element is not found, try with different index of the same upload element',
)
async def upload_cv(index: int, browser: BrowserContext):
    path = str(CV.absolute())
    dom_el = await browser.get_dom_element_by_index(index)
    # ...
    try:
        await file_upload_el.set_input_files(path)
        msg = f'Successfully uploaded file "{path}" to index {index}'
        return ActionResult(extracted_content=msg)
    except Exception as e:
        return ActionResult(error=f'Failed to upload file to index {index}')

async def main():
    ground_task = (
        'You are a professional job finder. '
        '1. Read my cv with read_cv'
        'find ml internships in and save them to a file'
        'search at company:'
    )
    tasks = [
        ground_task + '\n' + 'Google',
        # ...
    ]

    agents = []
    for task in tasks:
        agent = Agent(task=task, llm=model, controller=controller, browser=browser)
        agents.append(agent)

    await asyncio.gather(*[agent.run() for agent in agents])
View full example

Find Influencer Profiles
Extract a username from a TikTok video URL and search the web for associated social media profiles.

from pydantic import BaseModel
import httpx
from browser_use import Agent, Controller
from browser_use.agent.views import ActionResult

class Profile(BaseModel):
    platform: str
    profile_url: str

class Profiles(BaseModel):
    profiles: list[Profile]

controller = Controller(exclude_actions=['search_google'], output_model=Profiles)

@controller.registry.action('Search the web for a specific query')
async def search_web(query: str):
    keys_to_use = ['url', 'title', 'content', 'author', 'score']
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'https://asktessa.ai/api/search',
            headers=headers,
            json={'query': query},
        )

    final_results = [
        {key: source[key] for key in keys_to_use if key in source}
        for source in await response.json()['sources']
        if source['score'] >= 0.2
    ]
    # ...
    return ActionResult(extracted_content=result_text, include_in_memory=True)

async def main():
    task = (
        'Go to this tiktok video url, open it and extract the @username from the resulting url. Then do a websearch for this username to find all his social media profiles. Return me the links to the social media profiles with the platform name.'
        ' https://www.tiktokv.com/share/video/7470981717659110678/  '
    )
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, controller=controller)

    history = await agent.run()

    result = history.final_result()
    if result:
        parsed: Profiles = Profiles.model_validate_json(result)

        for profile in parsed.profiles:
            print(f'Platform: {profile.platform}')
            print(f'Profile URL: {profile.profile_url}')
View full example

Google Sheets
Automate interactions with Google Sheets, including opening sheets, reading/writing cell data, and clearing ranges.

from browser_use import ActionResult, Agent, Controller
from browser_use.browser.context import BrowserContext

controller = Controller()

def is_google_sheet(page) -> bool:
    return page.url.startswith('https://docs.google.com/spreadsheets/')

@controller.registry.action('Google Sheets: Open a specific Google Sheet')
async def open_google_sheet(browser: BrowserContext, google_sheet_url: str):
    page = await browser.get_current_page()
    if page.url != google_sheet_url:
        await page.goto(google_sheet_url)
        await page.wait_for_load_state()
    if not is_google_sheet(page):
        return ActionResult(error='Failed to open Google Sheet, are you sure you have permissions to access this sheet?')
    return ActionResult(extracted_content=f'Opened Google Sheet {google_sheet_url}', include_in_memory=False)

@controller.registry.action('Google Sheets: Get the contents of a specific cell or range of cells', page_filter=is_google_sheet)
async def get_range_contents(browser: BrowserContext, cell_or_range: str):
    # ...
    await select_cell_or_range(browser, cell_or_range)
    await page.keyboard.press('ControlOrMeta+C')
    extracted_tsv = pyperclip.paste()
    return ActionResult(extracted_content=extracted_tsv, include_in_memory=True)

@controller.registry.action('Google Sheets: Input text into the currently selected cell', page_filter=is_google_sheet)
async def input_selected_cell_text(browser: BrowserContext, text: str):
    page = await browser.get_current_page()
    await page.keyboard.type(text, delay=0.1)
    await page.keyboard.press('Enter')
    # ...
    return ActionResult(extracted_content=f'Inputted text {text}', include_in_memory=False)

async def main():
    async with await browser.new_context() as context:
        model = ChatOpenAI(model='gpt-4o')

        researcher = Agent(
            task="""
                Google to find the full name, nationality, and date of birth of the CEO of the top 10 Fortune 100 companies.
                For each company, append a row to this existing Google Sheet: https://docs.google.com/spreadsheets/d/1INaIcfpYXlMRWO__de61SHFCaqt1lfHlcvtXZPItlpI/edit
                Make sure column headers are present and all existing values in the sheet are formatted correctly.
                Columns:
                    A: Company Name
                    B: CEO Full Name
                    C: CEO Country of Birth
                    D: CEO Date of Birth (YYYY-MM-DD)
                    E: Source URL where the information was found
            """,
            llm=model,
            browser_context=context,
            controller=controller,
        )
        await researcher.run()
View full example

Online Coding Agent
Implement a multi-agent system where one agent opens an online code editor and another writes and executes code.

from browser_use import Agent, Browser

async def main():
    browser = Browser()
    async with await browser.new_context() as context:
        model = ChatOpenAI(model='gpt-4o')

        # Initialize browser agent
        agent1 = Agent(
            task='Open an online code editor programiz.',
            llm=model,
            browser_context=context,
        )
        executor = Agent(
            task='Executor. Execute the code written by the coder and suggest some updates if there are errors.',
            llm=model,
            browser_context=context,
        )

        coder = Agent(
            task='Coder. Your job is to write and complete code. You are an expert coder. Code a simple calculator. Write the code on the coding interface after agent1 has opened the link.',
            llm=model,
            browser_context=context,
        )
        await agent1.run()
        await executor.run()
        await coder.run()
View full example

Post Twitter
Automate posting new tweets and replying to existing ones on X (Twitter).

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from dataclasses import dataclass

@dataclass
class TwitterConfig:
    """Configuration for Twitter posting"""
    openai_api_key: str
    chrome_path: str
    target_user: str  # Twitter handle without @
    message: str
    reply_url: str
    headless: bool = False
    model: str = 'gpt-4o-mini'
    base_url: str = 'https://x.com/home'

# Customize these settings
config = TwitterConfig(
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    chrome_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    target_user='XXXXX',
    message='XXXXX',
    reply_url='XXXXX',
    headless=False,
)

def create_twitter_agent(config: TwitterConfig) -> Agent:
    llm = ChatOpenAI(model=config.model, api_key=config.openai_api_key)

    browser = Browser(
        config=BrowserConfig(
            headless=config.headless,
            browser_binary_path=config.chrome_path,
        )
    )

    controller = Controller()

    # Construct the full message with tag
    full_message = f'@{config.target_user} {config.message}'

    # Create the agent with detailed instructions
    return Agent(
        task=f"""Navigate to Twitter and create a post and reply to a tweet.

        Here are the specific steps:

        1. Go to {config.base_url}. See the text input field at the top of the page that says "What's happening?"
        2. Look for the text input field at the top of the page that says "What's happening?"
        3. Click the input field and type exactly this message:
        "{full_message}"
        4. Find and click the "Post" button (look for attributes: 'button' and 'data-testid="tweetButton"')
        5. Do not click on the '+' button which will add another tweet.

        6. Navigate to {config.reply_url}
        7. Before replying, understand the context of the tweet by scrolling down and reading the comments.
        8. Reply to the tweet under 50 characters.
        """,
        llm=llm,
        controller=controller,
        browser=browser,
    )

async def main():
    agent = create_twitter_agent(config)
    await agent.run()
View full example

Scrolling Page
Perform various scrolling actions on a webpage, including scrolling by specific amounts or to a particular text string.

from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig

llm = ChatOpenAI(model='gpt-4o')

agent = Agent(
    task="Navigate to 'https://en.wikipedia.org/wiki/Internet' and scroll to the string 'The vast majority of computer'",
    llm=llm,
    browser=Browser(config=BrowserConfig(headless=False)),
)

async def main():
    await agent.run()
View full example

Shopping
Automate online grocery shopping, including searching for items, adding to cart, handling substitutions, and proceeding to checkout.

from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser

task = """
   ### Prompt for Shopping Agent – Migros Online Grocery Order

Objective:
Visit [Migros Online](https://www.migros.ch/en), search for the required grocery items, add them to the cart, select an appropriate delivery window, and complete the checkout process using TWINT.

Important:
- Make sure that you don't buy more than it's needed for each article.
- After your search, if you click  the "+" button, it adds the item to the basket.
..."""

browser = Browser()

agent = Agent(
    task=task,
    llm=ChatOpenAI(model='gpt-4o'),
    browser=browser,
)

async def main():
    await agent.run()
    input('Press Enter to close the browser...')
    await browser.close()
View full example

Twitter Post Using Cookies
Post to X (Twitter) by loading authentication cookies from a file to bypass manual login.

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

# Goal: Automates posting on X (Twitter) using stored authentication cookies.

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

browser = Browser(
	config=BrowserConfig()
)

file_path = os.path.join(os.path.dirname(__file__), 'twitter_cookies.txt')
context = BrowserContext(browser=browser, config=BrowserContextConfig(cookies_file=file_path))

async def main():
	agent = Agent(
		browser_context=context,
		task=('go to https://x.com. write a new post with the text "browser-use ftw", and submit it'),
		llm=llm,
		max_actions_per_step=4,
	)
	await agent.run(max_steps=25)
	input('Press Enter to close the browser...')
View full example

Web Voyager Agent
A general-purpose web navigation agent for tasks like flight booking, hotel searching, or course finding on various websites.

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

# Set LLM based on defined environment variables
if os.getenv('OPENAI_API_KEY'):
    llm = ChatOpenAI(
        model='gpt-4o',
    )
elif os.getenv('AZURE_OPENAI_KEY') and os.getenv('AZURE_OPENAI_ENDPOINT'):
    llm = AzureChatOpenAI(
        model='gpt-4o',
        api_version='2024-10-21',
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
        api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
    )
else:
    raise ValueError('No LLM found. Please set OPENAI_API_KEY or AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT.')

browser = Browser(
    config=BrowserConfig(
        headless=False,  # This is True in production
        disable_security=True,
        new_context_config=BrowserContextConfig(
            disable_security=True,
            minimum_wait_page_load_time=1,  # 3 on prod
            maximum_wait_page_load_time=10,  # 20 on prod
            no_viewport=False,
            window_width=1280,
            window_height=1100,
        ),
    )
)

TASK = """
Find and book a hotel in Paris with suitable accommodations for a family of four (two adults and two children) offering free cancellation for the dates of February 14-21, 2025. on https://www.booking.com/
"""

async def main():
    agent = Agent(
        task=TASK,
        llm=llm,
        browser=browser,
        validate_output=True,
        enable_memory=False,
    )
    history = await agent.run(max_steps=50)
    history.save_to_file('./tmp/history.json')
View full example

Wikipedia Banana To Quantum
Navigate Wikipedia by clicking links to get from a starting page (e.g., “Banana”) to a target page (e.g., “Quantum mechanics”) as quickly as possible.

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig

llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)

task = 'go to https://en.wikipedia.org/wiki/Banana and click on buttons on the wikipedia page to go as fast as possible from banna to Quantum mechanics'

browser = Browser(
	config=BrowserConfig(
		new_context_config=BrowserContextConfig(
			viewport_expansion=-1,
			highlight_elements=False,
		),
	),
)
agent = Agent(task=task, llm=llm, browser=browser, use_vision=False)

async def main():
	await agent.run()



16. API Reference
This chapter provides a comprehensive reference of the Browser-Use API classes, methods, and parameters.

Core Components
Agent
The primary class for controlling browser automation. Integrates LLM, browser control, and action execution.

class Agent:
    def __init__(
        self,
        task: str,                     # Natural language instruction for the agent to execute
        llm: BaseChatModel,            # LangChain chat model for decision-making
        browser: Browser | None = None,            # Optional browser instance to use (creates one if None)
        browser_context: BrowserContext | None = None,  # Optional browser context (creates one if None)
        controller: Controller = Controller(),     # Registry of available actions for the agent
        sensitive_data: Optional[Dict[str, str]] = None,  # Secure data, referenced via placeholders
        initial_actions: Optional[List[Dict[str, Dict[str, Any]]]] = None,  # Actions to execute before first LLM call
        register_new_step_callback: Optional[Callable] = None,  # Callback after each step
        register_done_callback: Optional[Callable] = None,  # Callback when agent completes
        register_external_agent_status_raise_error_callback: Optional[Callable] = None,  # For remote control
        use_vision: bool = True,       # Whether to use visual information from browser
        use_vision_for_planner: bool = False,  # Whether to use vision for planning steps
        save_conversation_path: Optional[str] = None,  # Path to save conversation history
        save_conversation_path_encoding: Optional[str] = 'utf-8',  # Encoding for saved conversations
        max_failures: int = 3,         # Maximum consecutive failures before stopping
        retry_delay: int = 10,         # Seconds to wait between retries
        override_system_message: Optional[str] = None,  # Replace default system message
        extend_system_message: Optional[str] = None,  # Append to default system message
        max_input_tokens: int = 128000,  # Maximum tokens for LLM context
        validate_output: bool = False,  # Verify output before finishing
        message_context: Optional[str] = None,  # Additional context for LLM
        generate_gif: bool | str = False,  # Create GIF of browser interactions
        available_file_paths: Optional[list[str]] = None,  # Files agent can access
        include_attributes: list[str] = [...],  # HTML attributes to include in DOM representation
        max_actions_per_step: int = 10,  # Maximum actions per LLM call
        tool_calling_method: ToolCallingMethod | None = 'auto',  # How to invoke tools ('auto', 'function_calling', 'raw', 'tools'). ToolCallingMethod is a Literal type.
        page_extraction_llm: Optional[BaseChatModel] = None,  # Model for page content extraction
        planner_llm: Optional[BaseChatModel] = None,  # Model for planning steps
        planner_interval: int = 1,     # Run planner every N steps
        is_planner_reasoning: bool = False,  # Show planner reasoning
        extend_planner_system_message: str | None = None, # Append to default planner system message
        injected_agent_state: Optional[AgentState] = None,  # Pre-configured state (AgentState will be defined later)
        context = None,                # Custom context object
        enable_memory: bool = True,    # Use memory management
        memory_config: MemoryConfig | None = None,  # Memory configuration (MemoryConfig is defined in Data Models/Configuration Models)
        save_playwright_script_path: str | None = None, # Path to save a Playwright script of the session
        source: str | None = None      # Source of the agent run, for telemetry
    )

    async def run(self, max_steps: int = 100, on_step_start: Optional[Callable[['Agent'], Awaitable[None]]] = None, on_step_end: Optional[Callable[['Agent'], Awaitable[None]]] = None) -> AgentHistoryList:
        """Execute the task with the given maximum number of steps."""

    async def step(self, step_info: Optional[AgentStepInfo] = None) -> None:
        """Execute a single step of the agent's decision-making process."""

    async def take_step(self) -> tuple[bool, bool]:
        """Take a step and return (is_done, is_valid)."""

    def add_new_task(self, new_task: str) -> None:
        """Add a new task to the agent's context."""

    def pause(self) -> None:
        """Pause the agent's execution."""

    def resume(self) -> None:
        """Resume the agent's execution after pausing."""

    def stop(self) -> None:
        """Stop the agent's execution."""

    async def get_next_action(self, input_messages: list[BaseMessage]) -> AgentOutput:
        """Get next action from LLM based on current state."""

    async def multi_act(self, actions: list[ActionModel], check_for_new_elements: bool = True) -> list[ActionResult]:
        """Execute multiple actions."""

    async def rerun_history(self, history: AgentHistoryList, max_retries: int = 3, skip_failures: bool = True, delay_between_actions: float = 2.0) -> list[ActionResult]:
        """Rerun a previously recorded agent history."""

    async def load_and_rerun(self, history_file: str | Path | None = None, **kwargs) -> list[ActionResult]:
        """Load an agent history from a file and rerun it."""

    def save_history(self, file_path: str | Path | None = None) -> None:
        """Save the current agent history to a file."""

    async def log_completion(self) -> None:
        """Log the completion of the task."""

    async def close(self) -> None:
        """Close all resources used by the agent, including the browser."""

    @property
    def message_manager(self) -> MessageManager: # MessageManager will be defined/referenced later
        """Access the agent's message manager."""
Browser
Manages browser instances and creates browser contexts.

class Browser:
    def __init__(
        self,
        config: BrowserConfig | None = None,  # Browser configuration
    )

    async def new_context(self, config: BrowserContextConfig | None = None) -> BrowserContext:
        """Create a new browser context (similar to an incognito window)."""

    async def get_playwright_browser(self) -> PlaywrightBrowser:
        """Get the underlying Playwright browser instance."""

    async def close(self) -> None:
        """Close the browser and release resources."""
BrowserConfig
Configuration settings for browser initialization.

class BrowserConfig:
    wss_url: str | None = None          # WebSocket URL for remote browser connection
    cdp_url: str | None = None          # Chrome DevTools Protocol URL for connection
    browser_class: str = 'chromium'     # Browser type ('chromium', 'firefox', 'webkit')
    browser_binary_path: str | None = None  # Path to browser executable
    chrome_remote_debugging_port: int | None = 9222 # Optional port for Chrome DevTools Protocol, defaults to 9222
    extra_browser_args: list[str] = []  # Additional browser launch arguments
    headless: bool = False              # Run without visible UI (not recommended)
    disable_security: bool = False      # Disable security features (e.g., CORS, CSP). Setting to True is dangerous and should be used with caution.
    deterministic_rendering: bool = False  # Make rendering consistent across platforms
    keep_alive: bool = False            # Keep browser open after context closes
    proxy: ProxySettings | None = None  # Proxy configuration
    new_context_config: BrowserContextConfig = BrowserContextConfig()  # Default context settings
BrowserContext
Represents an isolated browser session similar to an incognito window.

class BrowserContext:
    def __init__(
        self,
        browser: 'Browser',              # Parent browser instance
        config: BrowserContextConfig | None = None,  # Context configuration
        state: Optional[BrowserContextState] = None,  # Pre-configured state (BrowserContextState will be defined later)
    )

    async def close(self) -> None:
        """Close the browser context and release resources."""

    async def get_current_page(self) -> Page:
        """Get the currently active page/tab that the agent is interacting with."""

    async def get_agent_current_page(self) -> Page:
        """Get the page that the agent is currently working with, ensuring recovery if the tab reference is invalid."""

    async def get_page_html(self) -> str:
        """Get the HTML content of the current page."""

    async def take_screenshot(self, full_page: bool = False) -> str:
        """Capture screenshot as base64-encoded string."""

    async def remove_highlights(self) -> None:
        """Remove element highlighting from page."""

    async def navigate_to(self, url: str) -> None:
        """Navigate to a URL and wait for load."""

    async def refresh_page(self) -> None:
        """Reload the current page."""

    async def go_back(self) -> None:
        """Navigate to previous page in history."""

    async def go_forward(self) -> None:
        """Navigate to next page in history."""

    async def wait_for_element(self, selector: str, timeout: float = 5000.0) -> None:
        """Wait for element to appear on page."""

    async def get_state(self, cache_clickable_elements_hashes: bool = False) -> BrowserState:
        """Get complete state of the browser for agent.
           cache_clickable_elements_hashes: If True, cache hashes of clickable elements to identify new elements in subsequent states.
        """

    async def get_selector_map(self) -> dict:
        """Get map of element indices to DOM nodes."""

    async def get_dom_element_by_index(self, index: int) -> DOMElementNode:
        """Get DOM element by highlight index."""

    async def get_locate_element(self, element: DOMElementNode) -> Optional[ElementHandle]:
        """Find element handle from DOM element."""

    async def get_locate_element_by_css_selector(self, css_selector: str) -> Optional[ElementHandle]:
        """Find element by CSS selector."""

    async def get_locate_element_by_xpath(self, xpath: str) -> Optional[ElementHandle]:
        """Find element by XPath."""

    async def get_locate_element_by_text(self, text: str, nth: Optional[int] = 0, element_type: str = None) -> Optional[ElementHandle]:
        """Find element by visible text content."""

    async def get_tabs_info(self) -> list[TabInfo]:
        """Get information about all open tabs."""

    async def is_file_uploader(self, element_node: DOMElementNode, max_depth: int = 3, current_depth: int = 0) -> bool:
        """Check if element is a file upload input."""

    async def switch_to_tab(self, page_id: int) -> None:
        """Switch to specified tab by ID."""

    async def create_new_tab(self, url: str = "about:blank") -> None:
        """Open a new tab with specified URL."""

    async def close_current_tab(self) -> None:
        """Close the agent's current tab."""

    async def execute_javascript(self, script: str) -> Any:
        """Execute JavaScript code on the agent's current page."""

    async def get_page_structure(self) -> str:
        """Get a debug view of the page structure including iframes."""

    async def get_element_by_index(self, index: int) -> Optional[ElementHandle]:
        """Get a Playwright ElementHandle by its highlight index."""

    async def save_cookies(self) -> None:
        """Save current browser context cookies to the file specified in BrowserContextConfig."""

    async def get_scroll_info(self, page: Page) -> tuple[int, int]:
        """Get the number of pixels scrollable above and below the current viewport on the given page."""

    async def reset_context(self) -> None:
        """Resets the browser context, clearing cookies, storage, and re-initializing the session."""
BrowserContextConfig
Configuration settings for browser contexts.

class BrowserContextConfig:
    cookies_file: str | None = None     # Path to cookies file for persistence
    minimum_wait_page_load_time: float = 0.25  # Minimum seconds to wait for page load
    wait_for_network_idle_page_load_time: float = 0.5  # Wait for network to quiet down
    maximum_wait_page_load_time: float = 5  # Maximum seconds to wait for page load
    wait_between_actions: float = 0.5   # Seconds to wait between actions
    disable_security: bool = True       # Disable security features
    window_width: int = 1280            # Default browser window width
    window_height: int = 1100           # Default browser window height
    no_viewport: bool = True  # When True (default for headful), browser window size determines viewport. If False, a fixed viewport (width/height above) is enforced.
    save_recording_path: str | None = None  # Path to save video recording
    save_downloads_path: str | None = None  # Path to save downloaded files
    save_har_path: str | None = None    # Path to save HAR network logs
    trace_path: str | None = None       # Path to save Playwright traces
    locale: str | None = None           # Browser locale (e.g., 'en-US')
    user_agent: str | None = None       # User agent string. If None, Playwright's default is used.
    highlight_elements: bool = True     # Visually highlight elements
    viewport_expansion: int = 0       # Pixels to expand viewport for DOM capture. 0 means only visible elements.
    allowed_domains: list[str] | None = None  # Restrict navigation to specific domains
    include_dynamic_attributes: bool = True  # Include dynamic attributes in selectors
    http_credentials: dict[str, str] | None = None  # HTTP Basic Auth credentials
    keep_alive: bool = False            # Keep context alive after agent finishes
    is_mobile: bool | None = None       # Emulate mobile device
    has_touch: bool | None = None       # Emulate touch screen
    geolocation: dict | None = None     # Emulate geolocation
    permissions: list[str] = ['clipboard-read', 'clipboard-write']  # Browser permissions to grant
    timezone_id: str | None = None      # Time zone ID (e.g., 'America/New_York')
    force_new_context: bool = False     # Forces a new browser context, even if one could be reused (e.g. with CDP).
Controller
Registry of functions/actions available to the agent. The controller utilizes a Registry instance (accessible via the registry attribute) for managing actions.

class Controller:
    def __init__(
        self,
        exclude_actions: list[str] = [],  # Actions to exclude from registration
        output_model: Optional[Type[BaseModel]] = None,  # Custom output model
    )

    # Decorator for registering actions
    def action(self, description: str, param_model = None, domains = None, page_filter = None):
        """Register a function as an action available to the agent."""

    # Registry of available actions
    registry: Registry
Registry
Core registry for actions that can be used by agents. Typically accessed via Controller.registry.

class Registry:
    def __init__(self, exclude_actions: list[str] | None = None):
        """Initialize registry, optionally excluding specific actions."""

    # Decorator for registering actions
    def action(self, description: str, param_model = None, domains = None, page_filter = None):
        """Register a function as an action with optional domain/page filters."""

    # Create Pydantic model for actions
    def create_action_model(self, include_actions: Optional[list[str]] = None, page = None) -> Type[ActionModel]:
        """Create a Pydantic model containing available actions."""

    # Get string description of actions for prompt
    def get_prompt_description(self, page = None) -> str:
        """Get textual description of available actions for LLM prompts."""
SystemPrompt
Provides the system message for the Agent, used to instruct the LLM on its role, capabilities, and constraints.

class SystemPrompt:
    def __init__(
        self,
        action_description: str,                     # String describing all available actions
        max_actions_per_step: int = 10,          # Maximum number of actions the agent can take in a single step
        override_system_message: Optional[str] = None,  # Completely replace the default system message with this string
        extend_system_message: Optional[str] = None     # Append this string to the default system message
    ):
        """Initializes the SystemPrompt.

        Args:
            action_description: A string detailing the actions available to the agent.
            max_actions_per_step: The maximum number of actions the agent can perform in one step.
            override_system_message: If provided, this string will be used as the entire system message, ignoring the default template.
            extend_system_message: If provided, this string will be appended to the generated system message.
        """

    def get_system_message(self) -> SystemMessage:
        """Get the SystemMessage object to be used by the LLM.

        Returns:
            SystemMessage: The LangChain SystemMessage object containing the formatted prompt.
        """
DOM Components
Services and models for interacting with the Document Object Model.

class DOMService:
    def __init__(self, page: 'Page'):
        """Initialize DOM service for a Playwright page."""

    async def get_clickable_elements(self, highlight_elements: bool = True, focus_element: int = -1, viewport_expansion: int = 0) -> DOMState:
        """Get clickable elements from the page DOM. Returns a DOMState object."""

    async def get_cross_origin_iframes(self) -> list[str]:
        """Get a list of URLs for cross-origin iframes within the current page."""

    async def _build_dom_tree(self, highlight_elements: bool, focus_element: int, viewport_expansion: int) -> tuple[DOMElementNode, SelectorMap]:
        """Build DOM tree representation with interactive elements."""

    async def _construct_dom_tree(self, eval_page: dict) -> tuple[DOMElementNode, SelectorMap]:
        """Construct a Python DOM tree from JavaScript evaluation."""
@dataclass
class CoordinateSet:
    x: int                            # X-coordinate of the top-left corner
    y: int                            # Y-coordinate of the top-left corner
    width: int                        # Width of the area
    height: int                       # Height of the area
@dataclass
class ViewportInfo:
    width: int                        # Width of the viewport
    height: int                       # Height of the viewport
@dataclass
class DOMElementNode:
    tag_name: str                   # HTML tag name (e.g., 'div', 'a')
    xpath: str                       # XPath to the element
    attributes: Dict[str, str]       # HTML attributes
    children: List[DOMBaseNode]      # Child nodes (DOMBaseNode is a base for DOMElementNode and DOMTextNode)
    is_visible: bool                 # Whether element is visible
    parent: Optional['DOMElementNode']  # Parent node
    is_interactive: bool = False     # Whether element is interactive
    is_top_element: bool = False     # Whether element is visually on top
    is_in_viewport: bool = False     # Whether in current viewport
    shadow_root: bool = False        # Whether element has shadow DOM
    highlight_index: Optional[int] = None  # Index for highlighting
    viewport_coordinates: Optional[CoordinateSet] = None  # Viewport coordinates
    page_coordinates: Optional[CoordinateSet] = None  # Page coordinates
    viewport_info: Optional[ViewportInfo] = None  # Viewport information for the element's frame/document
    is_new: bool | None = None       # Whether this element is new since the last state update (useful for agent memory)

    def get_all_text_till_next_clickable_element(self, max_depth: int = -1) -> str:
        """Get all text content up to next interactive element."""

    def clickable_elements_to_string(self, include_attributes: list[str] | None = None) -> str:
        """Convert clickable elements to string representation."""

    def get_file_upload_element(self, check_siblings: bool = True) -> Optional['DOMElementNode']:
        """Checks if the current element or its children (or siblings if check_siblings is True) is an input element of type 'file'."""
# SelectorMap is a type alias for Dict[int, DOMElementNode]
# It maps a highlight_index to its corresponding DOMElementNode.
SelectorMap = Dict[int, DOMElementNode]
@dataclass
class DOMState:
    element_tree: DOMElementNode      # The root of the DOM tree representation
    selector_map: SelectorMap         # A map from highlight_index to DOMElementNode
Message & Memory Components
Manages conversation history and memory for the agent. The Agent exposes a message_manager property. Memory is configured via MemoryConfig passed to the Agent.

MessageManager
The MessageManager class is responsible for handling the flow of messages to and from the language model, including managing context length and incorporating state information. An instance of this class is accessible via Agent.message_manager.

class MessageManager:
    def __init__(
        self,
        task: str,                               # The agent's task
        system_message: SystemMessage,           # System message for LLM
        settings: MessageManagerSettings = MessageManagerSettings(),  # Configuration for the message manager (defined in Default Settings)
        state: MessageManagerState = MessageManagerState(),        # Initial state for the message manager (MessageManagerState is defined in Data Models)
    )

    def add_new_task(self, new_task: str) -> None:
        """Add a new task to the conversation, informing the LLM of the change."""

    def add_state_message(
        self,
        state: BrowserState,                     # Current browser state
        result: list[ActionResult] | None = None,  # Result from the last action(s)
        step_info: Optional[AgentStepInfo] = None, # Information about the current step (AgentStepInfo is defined in Data Models)
        use_vision: bool = True                  # Whether to include visual (screenshot) information in the message
    ) -> None:
        """Add browser state information to the conversation history."""

    def add_model_output(self, model_output: AgentOutput) -> None:
        """Add the language model's output (thoughts and actions) to conversation history."""

    def add_plan(self, plan: str | None, position: int | None = None) -> None:
        """Adds a plan (typically from a planner agent) into the message history at the specified position."""

    def get_messages(self) -> List[BaseMessage]:
        """Get the current list of messages prepared for the LLM, after context management."""

    def cut_messages(self) -> None:
        """Reduce message history to fit within token limits, typically by truncating the last state message or removing images."""

    def add_tool_message(self, content: str, message_type: str | None = None, **additional_kwargs: Any) -> None:
        """Adds a ToolMessage to the history, usually representing the output of a tool call."""
Memory
The Memory class handles the creation and management of procedural memory for the agent, helping to consolidate past interactions into a summarized form. This is an internal component of the Agent when memory is enabled. Its behavior is configured through the MemoryConfig object.

class Memory:
    def __init__(
        self,
        message_manager: MessageManager,    # The MessageManager instance to work with
        llm: BaseChatModel,                 # The language model used for summarization
        config: MemoryConfig | None = None, # Configuration for memory (MemoryConfig is defined in Data Models/Configuration Models)
    )

    def create_procedural_memory(self, current_step: int) -> None:
        """Consolidates messages from the MessageManager's history to create or update procedural memory,
           replacing older messages with a summarized version.
        """
Data Models
Action Models
Models related to agent actions and responses.

class ActionResult:
    is_done: bool | None = False       # Whether task is complete
    success: bool | None = None        # Whether the 'done' action indicated overall task success (True if successful, False if not, None if not a 'done' action or not applicable)
    extracted_content: Optional[str] = None  # Content extracted from page
    error: Optional[str] = None        # Error message if action failed
    include_in_memory: bool = False    # Whether to include in memory
class AgentOutput:
    current_state: AgentBrain          # Agent's thought process
    action: List[ActionModel]          # Actions to execute. ActionModel is a base type; specific actions (e.g., click_element_by_index) will have their own parameter models.
class AgentBrain:
    evaluation_previous_goal: str      # Evaluation of previous step
    memory: str                        # Agent's memory of past events
    next_goal: str                     # Next goal to accomplish
Agent History Models
Models for tracking agent execution history.

class AgentHistoryList:
    history: List[AgentHistory]        # List of history items

    def is_done(self) -> bool:
        """Check if agent has completed task based on the last action result."""

    def is_successful(self) -> bool | None:
        """Check if the agent completed the task successfully. Returns True if successful, False if not, None if not done yet."""

    def final_result(self) -> Optional[str]:
        """Get final result text from the last action if the task is done."""

    def errors(self) -> list[str | None]:
        """Get all error messages from history, with None for steps without errors."""

    def has_errors(self) -> bool:
        """Check if history contains any errors."""

    def urls(self) -> list[str | None]:
        """Get all URLs visited during the agent's execution."""

    def screenshots(self) -> list[str | None]:
        """Get all base64 encoded screenshots taken."""

    def action_names(self) -> list[str]:
        """Get names of all actions executed."""

    def model_thoughts(self) -> list[AgentBrain]:
        """Get all agent thought processes (AgentBrain instances)."""

    def model_outputs(self) -> list[AgentOutput]:
        """Get all raw model outputs (AgentOutput instances)."""

    def model_actions(self) -> list[dict]:
        """Get all actions executed with their parameters."""

    def action_results(self) -> list[ActionResult]:
        """Get all action results."""

    def extracted_content(self) -> list[str]:
        """Get all content extracted by actions."""

    def total_duration_seconds(self) -> float:
        """Get total duration of all steps in seconds."""

    def total_input_tokens(self) -> int:
        """Get total approximate input tokens used across all steps."""

    def input_token_usage(self) -> list[int]:
        """Get approximate input token usage for each step."""

    def save_to_file(self, filepath: str | Path) -> None:
        """Save the agent history to a JSON file."""

    def save_as_playwright_script(
        self,
        output_path: str | Path,
        sensitive_data_keys: Optional[list[str]] = None,
        browser_config: Optional[BrowserConfig] = None,
        context_config: Optional[BrowserContextConfig] = None,
    ) -> None:
        """Generate and save a Playwright script based on the agent's history."""

    @classmethod
    def load_from_file(cls, filepath: str | Path, output_model: Type[AgentOutput]) -> 'AgentHistoryList':
        """Load an agent history from a JSON file."""

    def last_action(self) -> Optional[dict]:
        """Get the last action executed in the history, if any."""

    def model_actions_filtered(self, include: Optional[list[str]] = None) -> list[dict]:
        """Get model actions from history, filtered by a list of action names."""

    def number_of_steps(self) -> int:
        """Get the number of steps recorded in the history."""
class AgentHistory:
    model_output: Optional[AgentOutput]  # Agent's output (thoughts and actions)
    result: List[ActionResult]         # Results of actions
    state: BrowserStateHistory         # Browser state at the time of the step (BrowserStateHistory is an internal representation)
    metadata: Optional[StepMetadata] = None # Metadata for the step, like timing and token count (StepMetadata defined below)
Browser State Models
Models representing browser state.

class BrowserState:
    url: str                          # Current page URL
    title: str                        # Page title
    tabs: list[TabInfo]               # Open tabs
    element_tree: DOMElementNode      # DOM tree (DOMElementNode defined in DOM Components)
    selector_map: SelectorMap         # Map of element indices
    screenshot: Optional[str] = None  # Base64 encoded screenshot
    pixels_above: int = 0             # Pixels scrollable above the current viewport
    pixels_below: int = 0             # Pixels scrollable below the current viewport
    browser_errors: list[str] = []    # Browser console errors
class TabInfo:
    page_id: int                      # Tab ID
    url: str                          # Tab URL
    title: str                        # Tab title
    parent_page_id: Optional[int] = None # Optional ID of the parent page if this tab is a popup or iframe
Other Data Models
This section includes other Pydantic models that are part of the API, often used as parameters or return types for various components.

@dataclass
class AgentState:
    """Holds all state information for an Agent. Can be used for `injected_agent_state` in Agent `__init__`."""
    agent_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    n_steps: int = 1
    consecutive_failures: int = 0
    last_result: Optional[List[ActionResult]] = None
    history: AgentHistoryList = Field(default_factory=AgentHistoryList) # type: ignore
    last_plan: Optional[str] = None
    paused: bool = False
    stopped: bool = False
    message_manager_state: MessageManagerState = Field(default_factory=MessageManagerState) # type: ignore # MessageManagerState defined with MessageManager
@dataclass
class AgentStepInfo:
    """Information about the current step, passed to `Agent.step()`."""
    step_number: int
    max_steps: int

    def is_last_step(self) -> bool:
        """Check if this is the last step."""
class StepMetadata(BaseModel):
    """Metadata for a single agent step, found in `AgentHistory.metadata`."""
    step_start_time: float
    step_end_time: float
    input_tokens: int  # Approximate tokens from message manager for this step
    step_number: int

    @property
    def duration_seconds(self) -> float:
        """Calculate step duration in seconds."""
class MemoryConfig(BaseModel):
    """Configuration for procedural memory, used in `Agent.__init__`."""
    agent_id: str = Field(default='browser_use_agent', min_length=1)
    memory_interval: int = Field(default=10, gt=1, lt=100) # Interval in steps for creating memory summaries
    embedder_provider: Literal['openai', 'gemini', 'ollama', 'huggingface'] = 'huggingface'
    embedder_model: str = Field(min_length=2, default='all-MiniLM-L6-v2')
    embedder_dims: int = Field(default=384, gt=10, lt=10000)
    llm_provider: Literal['langchain'] = 'langchain'
    llm_instance: Optional[BaseChatModel] = None # The LLM instance to use for summarization
    vector_store_provider: Literal['faiss'] = 'faiss'
    vector_store_base_path: str = Field(default='/tmp/mem0') # Base path for vector store persistence
@dataclass
class BrowserContextState:
    """State of the browser context, can be used for `state` in `BrowserContext.__init__`."""
    target_id: Optional[str] = None  # CDP target ID
class ProxySettings(BaseModel):
    """Proxy server configuration, used in `BrowserConfig`."""
    server: str                         # Proxy server URL (e.g., "http://myproxy.com:3128" or "socks5://myproxy.com:3128")
    bypass: Optional[str] = None        # Comma-separated list of hosts to bypass proxy (e.g., "localhost,*.example.com")
    username: Optional[str] = None
    password: Optional[str] = None
Errors
Error classes for handling exceptions, and related utilities.

class BrowserError(Exception):
    """Base class for all browser errors"""
class URLNotAllowedError(BrowserError):
    """Error raised when a URL is not allowed"""
class LLMException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f'Error {status_code}: {message}')
    """Error raised for issues related to Language Model interactions."""
class AgentError:
    """Utility class for agent error handling. Not an exception itself."""

    @staticmethod
    def format_error(error: Exception, include_trace: bool = False) -> str:
        """Format error message with optional stack trace."""
Default Settings
Default setting classes for various components.

class AgentSettings:
    use_vision: bool                  # Use visual information
    use_vision_for_planner: bool      # Use vision for planning
    save_conversation_path: Optional[str]  # Save conversation to file
    save_conversation_path_encoding: Optional[str]  # File encoding
    max_failures: int                 # Max consecutive failures
    retry_delay: int                  # Seconds between retries
    override_system_message: Optional[str]  # Replace system message
    extend_system_message: Optional[str]  # Add to system message
    max_input_tokens: int             # Max tokens for input
    validate_output: bool             # Validate output before finishing
    message_context: Optional[str]    # Additional context
    generate_gif: bool | str          # Create GIF of execution
    available_file_paths: Optional[list[str]]  # Available files
    include_attributes: list[str]     # HTML attributes to include
    max_actions_per_step: int         # Max actions per step
    tool_calling_method: ToolCallingMethod | None = 'auto'  # How to invoke tools ('auto', 'function_calling', 'raw', 'tools'). ToolCallingMethod is a Literal type.
    page_extraction_llm: BaseChatModel  # Model for extraction
    planner_llm: Optional[BaseChatModel]  # Model for planning
    planner_interval: int             # Steps between planning
    is_planner_reasoning: bool        # Show planner reasoning
    extend_planner_system_message: str | None = None # Append to default planner system message
    save_playwright_script_path: str | None = None # Path to save a Playwright script of the session
class MessageManagerSettings:
    max_input_tokens: int = 128000    # Maximum input tokens
    estimated_characters_per_token: int = 3  # For token estimation
    image_tokens: int = 800           # Tokens per image
    include_attributes: list[str] = []  # HTML attributes to include
    message_context: Optional[str] = None  # Additional context
    sensitive_data: Optional[Dict[str, str]] = None  # Secure data
    available_file_paths: Optional[List[str]] = None  # Available files