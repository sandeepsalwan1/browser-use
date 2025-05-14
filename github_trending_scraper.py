import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

# Load environment variables
load_dotenv()

# Check if OpenAI API key is set
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError('OPENAI_API_KEY is not set. Add it to your .env file.')


class Repository(BaseModel):
    name: str
    description: str
    stars: str
    link: str
    technologies: str = ""  # Default to empty string to avoid None issues

class TweetSummary(BaseModel):
    text: str
    hashtags: str

class TrendingRepos(BaseModel):
    repos: List[Repository]
    summaries: List[TweetSummary] = Field(description="10 tweet-sized summaries of trends")
    date: str


from browser_use import Controller
controller = Controller(output_model=TrendingRepos)

async def main():

    browser_config = BrowserConfig(
        headless=False,  # Set to False to see the browser
    )
    
    browser = Browser(config=browser_config)
    
    llm = ChatOpenAI(
        model='gpt-4o',
        temperature=0.3,  # Slight increase for more creative summaries
    )
    
    task = """
    Go to https://github.com/trending and perform the following:
    
    1. Collect detailed information about the top 10 trending repositories:
       - Repository name
       - Description
       - Number of stars
       - Repository link
       - Key technologies used (look at languages shown, README content, etc.)
    
    2. For each repository, click through to examine:
       - README content to understand what the project does
       - Key technologies and frameworks used
       - The domain or field the project addresses (AI, web development, etc.)
       - What problem it solves or innovation it brings
    
    3. After analyzing ALL repositories, identify common themes, technologies, and trends.
    
    4. Create 10 DIFFERENT tweet-sized summaries (maximum 280 characters each) that:
       - Each focus on a different aspect or trend you discovered
       - Some should highlight specific repositories
       - Some should discuss technology trends overall
       - Some should mention surprising or interesting findings
       - All should include relevant hashtags
       
    5. Format your output as requested by the output model, with:
       - The repositories data in the 'repos' field
       - The 10 tweet summaries in the 'summaries' field as objects with 'text' and 'hashtags' properties
       - Today's date in the 'date' field
    """
    
    # Create and run the agent
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        controller=controller
    )
    
    # Run the agent
    history = await agent.run()
    
    # Process and display results
    result = history.final_result()
    if result:
        try:
            parsed = TrendingRepos.model_validate_json(result)
            
            # Print header
            print("\n=== GITHUB TRENDING SUMMARY ===")
            print(f"Date: {parsed.date}")
            
            # Print summaries
            print("\n=== TWEET-SIZED SUMMARIES ===")
            for i, summary in enumerate(parsed.summaries, 1):
                print(f"\n{i}. {summary.text}")
                print(f"   Hashtags: {summary.hashtags}")
          
            print("\n=== TOP TRENDING REPOSITORIES ===")
            for i, repo in enumerate(parsed.repos, 1):
                print(f"{i}. [{repo.name}]({repo.link}) - {repo.stars}")
                print(f"   {repo.description}")
                print(f"   Technologies: {repo.technologies}")
                print()
                
            # Save as markdown file
            filename = f"github_trending_{datetime.now().strftime('%Y%m%d')}.md"
            with open(filename, "w") as f:
                f.write(f"# GitHub Trending - {parsed.date}\n\n")
                
                f.write("## Tweet-Sized Summaries\n\n")
                for i, summary in enumerate(parsed.summaries, 1):
                    f.write(f"### Tweet {i}\n")
                    f.write(f"{summary.text}\n\n")
                    f.write(f"**Hashtags:** {summary.hashtags}\n\n")
                
                f.write("## Top Repositories\n\n")
                for repo in parsed.repos:
                    f.write(f"### [{repo.name}]({repo.link}) - {repo.stars}\n")
                    f.write(f"{repo.description}\n\n")
                    f.write(f"**Technologies:** {repo.technologies}\n\n")
            
            print(f"\nMarkdown report saved to {filename}")
            
        except Exception as e:
            print(f"Error processing results: {e}")
            print("Raw result:", result)
    else:
        print("No results obtained from the agent.")
    
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 