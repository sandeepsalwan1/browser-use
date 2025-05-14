# Minimal Audio Waveform Visualizer

A simple tool to download an audio file and create waveform visualizations using browser-use.

## What It Does

1. Downloads a sample arcade game over sound from Mixkit.co (no login required)
2. Creates waveform visualizations in three different styles:
   - Bars (classic style)
   - Wave (filled area style)
   - Outline (contour style)
3. Saves both the audio file and visualizations locally

## Requirements

- Python 3.8+
- Required packages:
  - browser-use
  - requests
  - langchain-openai
  - OpenAI API key (for GPT-4o)

## Quick Start

1. Install requirements:

```bash
pip install browser-use requests langchain-openai
```

2. Set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_api_key_here
```

3. Run the minimal visualizer:

```bash
python minimal_visualizer.py
```

4. Check the output in:
   - `downloads/` - Contains the audio file
   - `visualizations/` - Contains the visualization images (bars.png, wave.png, outline.png)

## How It Works

This minimal version:
1. Downloads an audio file directly with requests (no browser needed for this step)
2. Uses browser-use and the Web Audio API to visualize the audio waveform
3. Creates screenshots of each visualization style (bars, wave, outline)

## Troubleshooting

If you encounter any issues:
1. Make sure you have the latest version of browser-use installed
2. Check that your OpenAI API key is correctly set
3. Make sure the visualizer.html file is in the same directory as the script 