from TTS.api import TTS
import torch

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize TTS with XTTS-v2 model
# XTTS-v2 is one of the best models for voice cloning
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Test basic TTS without voice cloning
text = "Hello, this is XTTS-v2 speaking! It's a powerful text-to-speech model."
print(f"Generating audio for: {text}")

# Generate audio
wav = tts.tts(text=text)
tts.save_wav(wav, "xtts_v2_basic.wav")
print("Basic TTS saved as xtts_v2_basic.wav")

# Test voice cloning (if you have a reference audio file)
# Uncomment the following lines if you have a reference.wav file
"""
print("\nTesting voice cloning...")
wav_cloned = tts.tts(
    text="This is XTTS-v2 with voice cloning! It should sound like the reference voice.",
    speaker_wav="reference.wav",  # Path to your reference audio
    language="en"
)
tts.save_wav(wav_cloned, "xtts_v2_cloned.wav")
print("Voice cloning saved as xtts_v2_cloned.wav")
"""

print("\nXTTS-v2 test completed!")
print("Files created:")
print("  - xtts_v2_basic.wav")
# print("  - xtts_v2_cloned.wav")  # Uncomment if voice cloning was used 