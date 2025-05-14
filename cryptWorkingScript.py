import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import BaseModel
from typing import List

# Load environment variables (for API keys)
load_dotenv()

# Define the output model structure
class Product(BaseModel):
    name: str
    price: str
    url: str
    category: str

class Catalog(BaseModel):
    products: List[Product]

async def main():
    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.0,
    )
    #    Go to Gap website (https://www.gap.com) and 
    # Define the task for scraping Gap catalog
    task = """
    Collect information about products from their catalog:
    
    1. Navigate to the Gap website homepage
    2. Handle any cookie consent or popup notifications if they appear
    3. Go to the Men's section
    4. Choose a category like "T-shirts" or "Jeans"
    5. Extract details for at least 5 products including:
       - Product name
       - Price
       - Product URL
       - Category
    6. Structure the data in the specified format
    
    If you encounter any rate limiting or errors, try refreshing the page or navigating to a different section.
    """
    
    # Create a controller with the custom output model
    from browser_use import Controller
    controller = Controller(output_model=Catalog)
    
    # Create the agent
    agent = Agent(
        task=task,
        llm=llm,
        controller=controller,
    )
    
    # Run the agent
    history = await agent.run()
    
    # Print the final result
    result = history.final_result()
    if result:
        try:
            parsed = Catalog.model_validate_json(result)
            print("\n--- GAP CATALOG PRODUCTS ---")
            for i, product in enumerate(parsed.products, 1):
                print(f"\nProduct {i}:")
                print(f"Name:     {product.name}")
                print(f"Price:    {product.price}")
                print(f"URL:      {product.url}")
                print(f"Category: {product.category}")
        except Exception as e:
            print(f"Error parsing result: {e}")
            print("Raw result:", result)
    else:
        print("No results obtained")

if __name__ == "__main__":
    asyncio.run(main())
