import streamlit as st
import tempfile
import os
import whisper
import librosa
import json
from pathlib import Path

def load_model(model_size="base"):
    return whisper.load_model(model_size)

def load_audio_to_array(audio_bytes, original_ext):
    with tempfile.NamedTemporaryFile(delete=False, suffix=original_ext) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name
    
    y, sr = librosa.load(tmp_path, sr=16000, mono=True)
    return y, sr, tmp_path

def generate_srt(segments, filename):
    srt_content = ""
    for i, segment in enumerate(segments):
        start, end, text = segment["start"], segment["end"], segment["text"].strip()
        srt_content += f"{i+1}\n{start:.2f} --> {end:.2f}\n{text}\n\n"
    
    srt_path = os.path.join(tempfile.gettempdir(), f"{Path(filename).stem}.srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_path

def main():
    st.title("Audio to Subtitles Converter")
    
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])
    
    if audio_file:
        st.audio(audio_file, format=f"audio/{Path(audio_file.name).suffix[1:]}")
        
        if st.button("Convert to Subtitles"):
            st.write("Processing...")
            
            audio_data, sr, tmp_path = load_audio_to_array(audio_file.read(), Path(audio_file.name).suffix)
            model = load_model("base")
            result = model.transcribe(audio_data)
            segments = result["segments"]
            
            srt_path = generate_srt(segments, audio_file.name)
            
            with open(srt_path, "r", encoding="utf-8") as f:
                st.text_area("Generated Subtitles", f.read(), height=200)
            
            with open(srt_path, "rb") as f:
                st.download_button("Download SRT", f.read(), f"{Path(audio_file.name).stem}.srt", "text/plain")
            
            os.unlink(tmp_path)
            os.unlink(srt_path)

if __name__ == "__main__":
    main()
