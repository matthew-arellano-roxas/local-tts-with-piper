import os
import pygame
import time
import wave
from piper.voice import PiperVoice

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "en_US-amy-medium.onnx")
CONFIG_PATH = os.path.join(BASE_DIR, "en_US-amy-medium.onnx.json")
OUTPUT_WAV = os.path.join(BASE_DIR, "output.wav")

def speak(text):
    # Validation
    if not os.path.exists(MODEL_PATH) or not os.path.exists(CONFIG_PATH):
        print(f"Error: Files missing.\nLooked in: {BASE_DIR}")
        return

    print("Files found! Synthesizing...")
    voice = PiperVoice.load(MODEL_PATH, config_path=CONFIG_PATH)

    # 2. Use synthesize_wav for a perfect WAV file
    # This automatically adds the DATA chunks that Pygame is looking for
    with wave.open(OUTPUT_WAV, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    print("Playing audio...")
    
    # 3. Play the file
    # Note: 'amy-medium' is 22050Hz, synthesize_wav handles this metadata
    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_WAV)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    print("Done!")

if __name__ == "__main__":
    speak("The quick brown fox jumps over the lazy dog.")