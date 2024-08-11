import librosa
import numpy as np
import moviepy.editor as mp
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch

def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_path = "audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

def generate_subtitles(audio_path):
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    audio, rate = librosa.load(audio_path, sr=16000)
    input_values = tokenizer(audio, return_tensors="pt", padding="longest").input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.decode(predicted_ids[0])
    return transcription

if __name__ == "__main__":
    video_path = "input_video.mp4"
    audio_path = extract_audio(video_path)
    subtitles = generate_subtitles(audio_path)
    print("Generated Subtitles:\n", subtitles)
