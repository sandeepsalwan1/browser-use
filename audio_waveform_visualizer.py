import asyncio
import os
import base64
import shutil
import time
from pathlib import Path
from typing import Dict, Any
from browser_use import Agent, Browser, BrowserConfig, Controller, ActionResult
from langchain_openai import ChatOpenAI

# Create directories for downloads and visualizations
DOWNLOADS_DIR = Path("./downloads")
DOWNLOADS_DIR.mkdir(exist_ok=True)
VISUALIZATIONS_DIR = Path("./visualizations")
VISUALIZATIONS_DIR.mkdir(exist_ok=True)

# Set up a controller with custom actions
controller = Controller()

@controller.action("Download and save audio file")
async def download_audio_file(audio_url: str, browser: Browser):
    """Download and save an audio file from the provided URL"""
    # Create a new tab for downloading
    page = await browser.get_current_page()
    
    try:
        # Setup download event listener
        async with page.expect_download(timeout=30000) as download_info:
            # Navigate to the audio URL which should trigger the download
            await page.goto(audio_url)
        
        # Get the download
        download = await download_info.value
        
        # Get suggested filename
        filename = download.suggested_filename
        file_path = DOWNLOADS_DIR / filename
        
        # Save the file
        await download.save_as(file_path)
        
        return ActionResult(extracted_content=str(file_path.absolute()))
    except Exception as e:
        # Fallback to fetch if download event doesn't work
        try:
            # Get filename from URL
            filename = audio_url.split("/")[-1]
            file_path = DOWNLOADS_DIR / filename
            
            # Use curl to download the file (more reliable for direct downloads)
            os.system(f"curl -L '{audio_url}' -o '{file_path}'")
            
            if file_path.exists():
                return ActionResult(extracted_content=str(file_path.absolute()))
            else:
                return ActionResult(extracted_content=f"Failed to download audio: {str(e)}")
        except Exception as e2:
            return ActionResult(extracted_content=f"Failed to download audio: {str(e2)}")

@controller.action("Visualize audio")
async def visualize_audio(audio_path: str, visualization_style: str = "bars", browser: Browser = None):
    """
    Open the visualizer HTML and render the audio waveform.
    
    Args:
        audio_path: Path to the audio file
        visualization_style: Style to use (bars, wave, outline)
    """
    # Validate visualization style
    if visualization_style not in ["bars", "wave", "outline"]:
        visualization_style = "bars"  # Default to bars if invalid style
    
    # Get absolute path to visualizer.html
    visualizer_path = Path("visualizer.html").absolute()
    file_url = f"file://{visualizer_path}"
    
    # Convert file path to URL format
    audio_url = f"file://{audio_path}"
    
    # Open visualizer in new tab
    page = await browser.get_current_page()
    await page.goto(file_url)
    
    # Wait for page to load
    await page.wait_for_load_state("domcontentloaded")
    
    # Run the visualization function with the audio file
    await page.evaluate(f'window.visualizeAudio("{audio_url}")')
    
    # Wait for visualization to complete
    try:
        # Wait for status to update indicating completion
        await page.wait_for_function(
            'document.getElementById("status").textContent.includes("complete")',
            timeout=15000
        )
        
        # Click the appropriate style button
        if visualization_style != "bars":  # "bars" is default and already active
            await page.click(f'.style-button[data-style="{visualization_style}"]')
            # Wait for style change to render
            await asyncio.sleep(0.5)
        
        # Wait a moment for the visualization to render fully
        await asyncio.sleep(1)
        
        # Take a screenshot
        timestamp = int(time.time())
        screenshot_filename = f"waveform_{visualization_style}_{timestamp}.png"
        screenshot_path = VISUALIZATIONS_DIR / screenshot_filename
        await page.screenshot(path=str(screenshot_path))
        
        # Try taking a second type of visualization if first one succeeds
        if visualization_style == "bars":
            # Try the wave style too
            await page.click('.style-button[data-style="wave"]')
            await asyncio.sleep(1)
            wave_screenshot_path = VISUALIZATIONS_DIR / f"waveform_wave_{timestamp}.png"
            await page.screenshot(path=str(wave_screenshot_path))
            
            return ActionResult(extracted_content={
                "main_visualization": str(screenshot_path),
                "wave_visualization": str(wave_screenshot_path),
                "audio_path": audio_path
            })
        
        return ActionResult(extracted_content={
            "visualization": str(screenshot_path),
            "audio_path": audio_path
        })
    
    except Exception as e:
        return ActionResult(extracted_content=f"Error visualizing audio: {str(e)}")

async def main():
    # Configure browser
    browser_config = BrowserConfig(
        headless=False,  # Set to True for headless operation
        window_width=1280,
        window_height=800,
        save_downloads_path=str(DOWNLOADS_DIR)  # Set download directory
    )
    
    browser = Browser(config=browser_config)
    
    # Configure LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create agent
    agent = Agent(
        task="""
        1. Go to https://mixkit.co/free-sound-effects/
        2. Browse the sound effects and pick a category (like "Game Sounds", "Transitions", or "Music")
        3. Find an interesting sound effect and click on it to preview it
        4. Locate the green download button and extract the direct download URL
        5. Use the "Download and save audio file" action to download the audio file
        6. Use the "Visualize audio" action with the downloaded audio file to create visualizations
        7. Examine the visualization results and return information about both the audio file and its visualizations
        """,
        llm=llm,
        controller=controller,
        browser=browser,
        use_vision=True
    )
    
    # Run the agent
    try:
        print("Starting the Audio Waveform Visualizer...")
        print("This script will:")
        print("1. Browse Mixkit.co for free sound effects")
        print("2. Download an audio file")
        print("3. Create waveform visualizations")
        print("\nRunning agent...\n")
        
        history = await agent.run()
        
        print("\n✅ Agent completed successfully!\n")
        
        # Process results
        result = history.final_result()
        if isinstance(result, Dict):
            print("📊 Visualizations created:")
            for key, path in result.items():
                if "visualization" in key and isinstance(path, str):
                    print(f"  - {os.path.basename(path)}: {path}")
            
            if "audio_path" in result:
                print(f"\n🔊 Audio file: {result['audio_path']}")
        else:
            print(f"Final result: {result}")
        
        print("\n📁 Check the 'downloads' folder for the audio file.")
        print("📁 Check the 'visualizations' folder for the waveform images.")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        # Clean up browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 