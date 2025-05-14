import asyncio
import os
import requests
import time
from pathlib import Path
from browser_use import Agent, Controller, ActionResult, Browser
from langchain_openai import ChatOpenAI

# Create directories
DOWNLOADS_DIR = Path("./downloads")
DOWNLOADS_DIR.mkdir(exist_ok=True)
VISUALIZATIONS_DIR = Path("./visualizations")
VISUALIZATIONS_DIR.mkdir(exist_ok=True)

# Direct URL to a free audio file from Mixkit
AUDIO_URL = "https://assets.mixkit.co/sfx/download/mixkit-arcade-retro-game-over-213.wav"

# Create custom controller with our actions
controller = Controller()

@controller.action("Save visualization screenshot")
async def save_visualization_screenshot(style_name: str, browser: Browser):
    """
    Take a screenshot of the current visualization and save it to the visualizations folder.
    
    Args:
        style_name: The name of the visualization style (bars, wave, outline)
        browser: The browser instance
    """
    try:
        # Generate timestamp for unique filename
        timestamp = int(time.time())
        filename = f"waveform_{style_name}_{timestamp}.png"
        filepath = VISUALIZATIONS_DIR / filename
        
        # Take screenshot using the browser's screenshot action
        await browser.take_screenshot(path=str(filepath))
        
        return ActionResult(
            extracted_content={
                "screenshot_path": str(filepath),
                "style": style_name,
                "message": f"Saved {style_name} visualization screenshot"
            }
        )
    except Exception as e:
        return ActionResult(
            extracted_content={
                "error": str(e),
                "message": f"Failed to save {style_name} visualization screenshot: {str(e)}"
            }
        )

async def main():
    print("Starting Simple Audio Waveform Visualizer...")
    
    # Step 1: Download the audio file directly
    print("\n1. Downloading audio file...")
    audio_filename = AUDIO_URL.split("/")[-1]
    audio_path = DOWNLOADS_DIR / audio_filename
    
    # Download using requests (more reliable than curl)
    response = requests.get(AUDIO_URL)
    with open(audio_path, "wb") as f:
        f.write(response.content)
    
    print(f"   ✅ Downloaded to: {audio_path}")
    
    # Step 2: Set up the agent to visualize the audio
    print("\n2. Setting up browser-use agent...")
    
    # Configure LLM - change model as needed
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create the agent
    agent = Agent(
        task=f"""
        Open the local HTML visualizer and visualize an audio file.
        
        1. Navigate to file://{Path("visualizer.html").absolute()}
        2. Wait for the page to load
        3. Run this JavaScript in the console:
           window.visualizeAudio("file://{audio_path}")
        4. Wait for the visualization to complete by looking for "complete" in the status text
        5. For each visualization style (bars, wave, outline):
           - Click on the style button
           - Wait briefly for the visualization to update
           - Use the "Save visualization screenshot" action to save the visualization
        6. Return information about which styles were captured
        """,
        llm=llm,
        controller=controller,
        use_vision=True
    )
    
    # Step 3: Run the agent to visualize the audio
    print("\n3. Running visualization agent...")
    try:
        history = await agent.run()
        
        print("\n✨ Visualization complete!")
        print(f"\nAudio file: {audio_path}")
        print(f"Check the visualizations saved to: {VISUALIZATIONS_DIR}")
        
        # Report results
        final_result = history.final_result()
        if final_result:
            print("\nAgent result:", final_result)
        else:
            print("\nNo explicit result returned")
            
            # Check if screenshots were taken
            screenshots = list(VISUALIZATIONS_DIR.glob("waveform_*.png"))
            if screenshots:
                print(f"Found {len(screenshots)} visualization screenshots:")
                for screenshot in screenshots:
                    print(f"  - {screenshot}")
            else:
                print("No visualization screenshots found.")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 