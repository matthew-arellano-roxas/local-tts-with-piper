# TTS Demo with Piper

This project shows two ways to use a local [Piper](https://github.com/rhasspy/piper) voice model in Python:

- `audio_file_speak.py` generates `output.wav` and plays it with `pygame`
- `stream_speak.py` streams speech directly to your speakers with `sounddevice`

The scripts are currently configured to use:

- `en_US-amy-medium.onnx`
- `en_US-amy-medium.onnx.json`

Both model files should stay in the same folder as the Python scripts.

## Download The Model Files

Download the voice files for `en_US-amy-medium` from Hugging Face:

- Model page: [Hugging Face - en_US-amy-medium](https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/amy/medium)
- `en_US-amy-medium.onnx`
- `en_US-amy-medium.onnx.json`

After downloading them, place both files in this project folder with the scripts.

## Project Files

- `audio_file_speak.py`
- `stream_speak.py`
- `en_US-amy-medium.onnx`
- `en_US-amy-medium.onnx.json`
- `output.wav`

## Requirements

- Python 3.10 or newer recommended
- A working audio output device
- Piper model files in the project folder

## Windows Setup

1. Open PowerShell in the project folder:

```powershell
cd c:\Users\Matthew\Documents\TTS
```

2. Install Python packages:

```powershell
py -m pip install piper-tts pygame numpy sounddevice
```

3. Make sure these files exist in the folder:

```text
en_US-amy-medium.onnx
en_US-amy-medium.onnx.json
```

## Linux Setup

1. Open a terminal in the project folder:

```bash
cd /path/to/TTS
```

2. Install system audio dependencies if needed.

For Debian or Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip portaudio19-dev libasound2-dev libsdl2-mixer-2.0-0
```

3. Install the Python packages:

```bash
python3 -m pip install piper-tts pygame numpy sounddevice
```

4. Make sure these files exist in the folder:

```text
en_US-amy-medium.onnx
en_US-amy-medium.onnx.json
```

## How To Use

### Windows

Generate a WAV file and play it:

```powershell
py audio_file_speak.py
```

Stream speech directly:

```powershell
py stream_speak.py
```

### Linux

Generate a WAV file and play it:

```bash
python3 audio_file_speak.py
```

Stream speech directly:

```bash
python3 stream_speak.py
```

## What Each Script Does

### `audio_file_speak.py`

- Loads the Piper voice model
- Synthesizes the sample text
- Saves the output to `output.wav`
- Plays the WAV file using `pygame`

The sample text is defined near the bottom of [audio_file_speak.py](c:/Users/Matthew/Documents/TTS/audio_file_speak.py):

```python
if __name__ == "__main__":
    speak("The quick brown fox jumps over the lazy dog.")
```

Replace the string with your own text.

### `stream_speak.py`

- Loads the same Piper voice model
- Synthesizes the sample text
- Streams audio directly to the output device using `sounddevice`

The sample text is defined near the bottom of [stream_speak.py](c:/Users/Matthew/Documents/TTS/stream_speak.py):

```python
if __name__ == "__main__":
    msg = "Success. The audio engine is now streaming correctly to your speakers."
    speak_streaming(msg)
```

Replace `msg` with your own text.

## Expected Output

- `audio_file_speak.py` creates or overwrites `output.wav`
- `stream_speak.py` plays audio without creating a WAV file first

## Troubleshooting

### `Error: Files missing`

Make sure these files are present in the same directory as the scripts:

- `en_US-amy-medium.onnx`
- `en_US-amy-medium.onnx.json`

### `ModuleNotFoundError`

Reinstall the Python dependencies.

Windows:

```powershell
py -m pip install piper-tts pygame numpy sounddevice
```

Linux:

```bash
python3 -m pip install piper-tts pygame numpy sounddevice
```

### No sound

- Check that your speakers or headphones are connected
- Make sure the correct audio device is selected
- Verify your system volume is not muted
- Close other apps that may be locking the audio device

On Linux, also make sure your audio backend is working correctly with ALSA or PulseAudio/PipeWire.

## Quick Start

### Windows

```powershell
cd c:\Users\Matthew\Documents\TTS
py -m pip install piper-tts pygame numpy sounddevice
py audio_file_speak.py
py stream_speak.py
```

### Linux

```bash
cd /path/to/TTS
python3 -m pip install piper-tts pygame numpy sounddevice
python3 audio_file_speak.py
python3 stream_speak.py
```
