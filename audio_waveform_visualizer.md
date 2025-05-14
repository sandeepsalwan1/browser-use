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
```

3. Set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:

```bash
python audio_waveform_visualizer.py
```

2. The script will:
   - Launch a browser and navigate to Mixkit.co
   - Find and download a sound effect
   - Generate waveform visualizations
   - Save everything to the downloads and visualizations folders

3. Check the output folders:
   - `downloads/`: Contains the downloaded audio files
   - `visualizations/`: Contains the waveform visualization images

## Visualization Styles

The script generates multiple visualization styles:

1. **Bars**: Traditional bar-style audio waveform
2. **Wave**: Smooth wave-style visualization with filled area
3. **Outline**: An outline style showing amplitude variations

## How It Works

This project uses:

- **browser-use**: For browser automation and navigation
- **LangChain + OpenAI API**: For intelligent navigation and decision making
- **Web Audio API**: For audio processing and waveform generation
- **HTML5 Canvas**: For drawing the visualizations

## Customization

You can modify the script to:

- Change visualization styles or colors in `visualizer.html`
- Add more sound effect sources
- Adjust browser settings in the `BrowserConfig`
- Modify the agent instructions to focus on specific sound categories

## License

This project uses sound effects from Mixkit.co, which are free to use.
The code is available under MIT license. 