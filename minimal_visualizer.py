import asyncio
import os
import requests
from pathlib import Path
from browser_use import Agent
from langchain_openai import ChatOpenAI

# Create directories
DOWNLOADS_DIR = Path("./downloads")
DOWNLOADS_DIR.mkdir(exist_ok=True)
VISUALIZATIONS_DIR = Path("./visualizations")
VISUALIZATIONS_DIR.mkdir(exist_ok=True)

# Direct URL to a free audio file from Mixkit
AUDIO_URL = "https://assets.mixkit.co/sfx/download/mixkit-arcade-retro-game-over-213.wav"

async def main():
    print("Starting Minimal Audio Waveform Visualizer...")
    
    # Step 1: Download the audio file directly
    print("\n1. Downloading audio file...")
    audio_filename = AUDIO_URL.split("/")[-1]
    audio_path = DOWNLOADS_DIR / audio_filename
    
    # Download using requests
    response = requests.get(AUDIO_URL)
    with open(audio_path, "wb") as f:
        f.write(response.content)
    
    print(f"   ✅ Downloaded to: {audio_path}")
    
    # Step 2: Set up the agent to visualize the audio
    print("\n2. Setting up browser-use agent...")
    
    # Configure LLM - change model as needed
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create the agent with a very simple task
    agent = Agent(
        task=f"""
        Follow these steps EXACTLY:
        
        1. Go to file://{Path("visualizer.html").absolute()}
        2. Wait for the page to load
        3. Once loaded, execute this JavaScript in the browser console: 
           window.visualizeAudio("file://{audio_path}")
        4. Wait for the visualization to complete (status message will show "complete")
        5. Take screenshots of the visualization in each style:
           a. Click the "Wave" button to switch to wave style
           b. Take a screenshot and save it to {VISUALIZATIONS_DIR}/wave.png
           c. Click the "Outline" button to switch to outline style
           d. Take a screenshot and save it to {VISUALIZATIONS_DIR}/outline.png
           e. Click the "Bars" button to switch back to bars style
           f. Take a screenshot and save it to {VISUALIZATIONS_DIR}/bars.png
        
        Do not explain what you're doing, just execute the steps precisely.
        """,
        llm=llm,
        use_vision=True
    )
    
    # Step 3: Run the agent to visualize the audio
    print("\n3. Running visualization agent...")
    try:
        await agent.run()
        
        # Check if screenshots were created
        expected_files = ["bars.png", "wave.png", "outline.png"]
        created_files = []
        
        for filename in expected_files:
            filepath = VISUALIZATIONS_DIR / filename
            if filepath.exists():
                created_files.append(filename)
        
        if created_files:
            print("\n✅ Visualization complete!")
            print(f"\nAudio file: {audio_path}")
            print(f"Created visualization screenshots:")
            for file in created_files:
                print(f"  - {VISUALIZATIONS_DIR / file}")
        else:
            print("\n⚠️ No screenshots were created. Check browser window for errors.")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 