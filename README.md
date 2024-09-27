# Real-time Sentiment Analysis 🎙️🧠💬

**Real-time Sentiment Analysis** is a Python-based tool that captures real-time audio input, converts it to text, and performs sentiment analysis on the spoken words. This project utilizes `PyAudio` for recording audio, `SpeechRecognition` for converting speech to text, and `nltk` (Natural Language Toolkit) to analyze the sentiment of the transcribed text. In a matter of seconds, you can capture speech and understand whether the sentiment is positive, negative, or neutral!

## Features 🚀
- **Real-time Audio Input**: Uses PyAudio to capture live speech from your microphone.
- **Speech to Text**: Converts spoken audio into text using the SpeechRecognition library.
- **Sentiment Analysis**: Analyzes the transcribed text to determine the sentiment (positive, negative, or neutral) using `nltk`.
- **Instant Feedback**: Provides sentiment results in just a few seconds.

## How It Works 🔍
1. **Capture Audio**: The program records real-time audio using your microphone.
2. **Convert Audio to Text**: Using Google Speech Recognition API via `SpeechRecognition`, the audio is transcribed into text.
3. **Perform Sentiment Analysis**: The transcribed text is passed through `nltk`'s sentiment analysis module, which outputs a sentiment score.
4. **Generate Sentiment Output**: Based on the analysis, the program will classify the sentiment as **positive**, **neutral**, or **negative** and display the result.

## Example Output
```bash
Recording audio...
Transcribing...
Transcription: "The service today was excellent, and I had a great experience."
Sentiment: The text_analyzer is positive.
