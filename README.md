# Jarvis: Voice-Activated Virtual Assistant

Jarvis is a voice-activated virtual assistant that can perform tasks like opening websites, playing music, fetching news, and handling general queries using Hugging Face's GPT-Neo model.

---

## Features
- Open popular websites like Google, YouTube, Facebook, and LinkedIn.
- Play songs from a predefined music library.
- Fetch the latest news headlines.
- Generate intelligent responses for general queries using Hugging Face GPT-Neo.

---

## Prerequisites
- Python 3.8 or above installed on your system.
- Internet connection (required for fetching news and using Hugging Face model).
- A compatible microphone for voice commands.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/jarvis-virtual-assistant.git
cd jarvis-virtual-assistant

2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

3. Install Required Libraries
Install the following libraries manually using pip:

pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install transformers
pip install torch

Library Overview:

SpeechRecognition: For voice-to-text conversion.
pyttsx3: For text-to-speech functionality.
requests: For fetching news via the NewsAPI.
transformers and torch: For Hugging Face GPT-Neo text generation.
4. Set Up the News API Key
Sign up at NewsAPI to get a free API key.
Replace the placeholder API_KEY in the main.py file with your own News API key:

API_KEY = "your_news_api_key_here"


5. Prepare the Music Library
Create a file called musicLibrary.py in the project folder. Define a dictionary with song names as keys and YouTube links as values:

music = {
    "song_name": "https://www.youtube.com/watch?v=example",
    "another_song": "https://www.youtube.com/watch?v=example2"
}

6. Run the Project
Start the virtual assistant:

python main.py

Usage
Launch the project using the command above.
Speak the wake word "Hello" to activate Jarvis.
Once activated, give commands such as:
"Open Google" to open Google in a browser.
"Play song_name" to play a song from your library.
"Fetch news" to listen to the latest news headlines.
Any general query like "What is coding?" to get an AI-generated response.
Project Code Overview
main.py
The primary script that:
Listens for user commands via the microphone.
Processes specific commands (like opening websites, playing music, fetching news).
Uses Hugging Face GPT-Neo for intelligent responses.
musicLibrary.py
A separate file where you define a dictionary mapping song names to YouTube URLs.
Troubleshooting
