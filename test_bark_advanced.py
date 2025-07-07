from bark import SAMPLE_RATE, generate_audio, preload_models
import scipy.io.wavfile as wavfile
import numpy as np

# Preload models (already downloaded)
preload_models()

# Test different voices and styles
texts = [
    "Hello, this is Bark TTS speaking with a natural voice!",
    "♪ [Music] This is a musical voice singing a beautiful melody ♪",
    "¡Hola! This is Bark speaking in Spanish with a Spanish accent!",
    "こんにちは！This is Bark speaking in Japanese with a Japanese accent!",
    "Bonjour! This is Bark speaking in French with a French accent!"
]

# Generate audio for each text
for i, text in enumerate(texts):
    print(f"Generating audio for: {text[:50]}...")
    audio_array = generate_audio(text)
    
    # Save each audio file
    filename = f"bark_output_{i+1}.wav"
    wavfile.write(filename, SAMPLE_RATE, audio_array)
    print(f"Saved as {filename}")

print("\nAll audio files generated successfully!")
print("Files created:")
for i in range(len(texts)):
    print(f"  - bark_output_{i+1}.wav") 