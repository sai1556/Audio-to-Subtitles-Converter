# Audio-to-Subtitles-Converter
📌 Project Overview

The Audio to Subtitles Converter is a Streamlit-based web application that converts audio files into subtitles in SRT, TXT, and JSON formats using OpenAI's Whisper model. This tool is useful for content creators, journalists, and anyone who needs accurate speech-to-text transcription with timestamped subtitles.
🚀 Features

    ✅ Upload audio files (MP3, WAV, M4A)
    ✅ Automatic speech-to-text transcription using Whisper
    ✅ Generate SRT subtitles with timestamps
    ✅ Basic noise reduction for improved accuracy
    ✅ Waveform visualization of the audio
    ✅ Editable transcript before exporting
    ✅ Download subtitles in SRT, TXT, and JSON formats

🔧 Tech Stack

    Python
    Streamlit (for the web interface)
    Whisper (for speech-to-text transcription)
    Librosa (for audio processing)
    Matplotlib (for waveform visualization)

📂 Dataset

The subtitle data is stored in eng_subtitles_database.db, containing a table zipfiles with the following columns:

    num: Unique subtitle ID
    name: Subtitle file name
    content: Binary compressed subtitle file (encoded in 'latin-1')

📜 Installation & Setup
1️⃣ Install Dependencies

Run the following command to install required packages:

pip install -r requirements.txt

2️⃣ Run the Application

streamlit run app.py

3️⃣ Use the Web Interface

    Upload an audio file
    Select the model size & language
    Click "Convert to Subtitles"
    Download the subtitles in your preferred format

📌 Future Enhancements

    Integrate Speech-to-Text API for better transcription accuracy.
    Enhance Chunking Strategy to improve contextual understanding.
    Deploy as a Web App using FastAPI or Streamlit.
