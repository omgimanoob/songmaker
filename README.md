
# SongMaker

SongMaker is a project that programmatically generates music from given lyrics using various open-source tools and libraries. This project utilizes TensorFlow, Magenta, MIDI processing libraries, and other audio tools to create a comprehensive pipeline for music creation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- ffmpeg (for audio processing)

### Steps

1. **Clone the repository:**

   \`\`\`sh
   git clone https://github.com/yomgimanoob/songmaker.git
   cd songmaker
   \`\`\`

2. **Create and activate a virtual environment:**

   \`\`\`sh
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

3. **Install the required packages:**

   \`\`\`sh
   pip install --upgrade pip
   pip install tensorflow magenta mido pretty_midi pydub
   \`\`\`

4. **Install ffmpeg:**

   \`\`\`sh
   sudo apt install ffmpeg
   \`\`\`

## Usage

1. **Generate a melody:**

   \`\`\`sh
   python generate_melody.py
   \`\`\`

2. **Add accompaniment (optional):**
   - You can use MuseScore or script it programmatically.

3. **Synthesize vocals:**
   - Use Synthesizer V or UTAU to input the lyrics and synchronize them with the melody.

4. **Combine and finalize:**

   \`\`\`sh
   python combine_tracks.py
   \`\`\`

### Example Scripts

- `generate_melody.py`: Script to generate a melody using Magenta.
- `add_accompaniment.py`: Script to add accompaniment to the generated melody.
- `synthesize_vocals.py`: Script to synthesize vocals using external tools.
- `combine_tracks.py`: Script to combine the melody, accompaniment, and vocals into a final song.

## Project Structure

\`\`\`plaintext
songmaker/
├── .gitignore
├── README.md
├── venv/
├── generate_melody.py
├── add_accompaniment.py
├── synthesize_vocals.py
├── combine_tracks.py
├── output/
│   ├── melody.mid
│   ├── accompaniment.mid
│   ├── vocals.wav
│   └── final_song.wav
└── requirements.txt
\`\`\`

## Features

- **Melody Generation**: Automatically generate melodies using Magenta.
- **Accompaniment**: Add chords and harmonies to your melodies.
- **Vocal Synthesis**: Synthesize vocals from given lyrics.
- **Track Combination**: Combine different musical elements into a final song.


