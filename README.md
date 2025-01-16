# Speech to Text Transcription System 🎙️➡️📜

## Overview 🎯

This project is a Speech-to-Text Transcription system that converts audio input into accurate text using **Machine Learning models** and the **AssemblyAI API**. Libraries like **pyaudio**, **wave**, **numpy**, and **matplotlib** are utilized for audio processing and visualization. 📈

## Features ✨

- **Audio-to-Text Conversion**: High-accuracy transcription of audio input. 🎧
- **API Integration**: Leveraged **AssemblyAI API** for speech recognition and enhanced performance. 🌐
- **Audio Processing**: Used libraries like **pyaudio** and **wave** for handling audio files. 🎶
- **Visualizations**: Incorporated **matplotlib** for audio signal visualization. 📊

## Technologies Used 💻

- **Backend**: Python, Django
- **Machine Learning**: Audio-to-text models with external API integration
- **Libraries**: AssemblyAI, pyaudio, wave, numpy, matplotlib

## Installation ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/speech-to-text-transcription.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```

## How It Works 🔄

1. **Audio Input**: Users upload an audio file or provide live input via a microphone. 🎙️
2. **Processing**: Audio data is preprocessed using **pyaudio** and **wave** libraries. 📦
3. **Transcription**: The processed audio is sent to the **AssemblyAI API**, which returns the text transcription. 📝
4. **Output**: The transcription is displayed on the web interface for the user to view or download. 🌟
