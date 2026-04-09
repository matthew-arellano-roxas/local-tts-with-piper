import os
import numpy as np
import sounddevice as sd
from piper.voice import PiperVoice

# 1. Setup Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "en_US-amy-medium.onnx")
CONFIG_PATH = os.path.join(BASE_DIR, "en_US-amy-medium.onnx.json")

def speak_streaming(text):
    if not os.path.exists(MODEL_PATH):
        print("Error: Model files missing.")
        return

    # 2. Load the voice engine
    print("Initializing Piper (v1.4.2)...")
    voice = PiperVoice.load(MODEL_PATH, config_path=CONFIG_PATH)

    # 3. Setup the Audio Stream
    # blocksize=1024 ensures a smooth flow on Windows
    stream = sd.OutputStream(
        samplerate=22050, 
        channels=1, 
        dtype='int16',
        blocksize=1024
    )
    stream.start()

    print(f"🎙️ Streaming: {text}")

    # 4. Convert Bytes to NumPy Array and Write
    for chunk in voice.synthesize(text):
        if hasattr(chunk, 'audio_int16_bytes'):
            # This line is the fix: convert the raw bytes into int16 integers
            audio_data = np.frombuffer(chunk.audio_int16_bytes, dtype=np.int16)
            stream.write(audio_data)
    
    # 5. Cleanup
    stream.stop()
    stream.close()
    print("Done.")

if __name__ == "__main__":
    msg = "Success. The audio engine is now streaming correctly to your speakers."
    speak_streaming(msg)