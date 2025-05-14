
"""
To use this script, you have to have a username and password for lichess.org.
You also have to enable keyboard input in the lichess.org settings.
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent, Browser, BrowserConfig

# Load environment variables
load_dotenv()

# Check if OpenAI API key is set
if not os.getenv('OPENAI_API_KEY'):
	raise ValueError('OPENAI_API_KEY is not set. Add it to your .env file.')

llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.2,
)

# Replace YOURUSERNAME and YOURPASSWORD with your actual lichess username and password
task = """
Go to lichess.org and play a chess game. Follow these steps:
1. Navigate to lichess.org
2. Click on "Sign in" at the top right
3. Log in with these credentials:
   - Username: YOURUSERNAME
   - Password: YOURPASSWORD
4. After logging in, click on "Play" at the top and then "Computer" to play against AI
5. Choose the easiest difficulty level (Stockfish level 1)
6. You will play as white. Make moves by:
   - Clicking on a piece and then its destination square
   - OR if available, type algebraic notation like "e4" or "Nf3" in the move input box
Here are some good opening moves you can try:
- "e4" (King's Pawn Opening)
- "d4" (Queen's Pawn Opening)
- "Nf3" (Réti Opening)
Continue making logical moves according to chess principles:
- Control the center
- Develop your pieces (knights and bishops first)
- Castle your king to safety
- Connect your rooks
- Avoid unnecessary pawn moves
Play at least 100 moves before concluding the game.
If you see an option to input moves by keyboard, feel free to use it. Otherwise, click the pieces to move them.
"""

# Initialize the agent with visible browser
agent = Agent(
	task=task,
	llm=llm,
	browser=Browser(config=BrowserConfig(headless=False)),  # Set headless=False to see the browser
)


async def main():
	# Run the agent
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main()) 