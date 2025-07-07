from bark import SAMPLE_RATE, generate_audio, preload_models
import scipy.io.wavfile as wavfile

# Preload models (downloads on first run)
preload_models()

text_prompt = "Hello, this is Bark TTS speaking!"
audio_array = generate_audio(text_prompt)

wavfile.write("bark_output.wav", SAMPLE_RATE, audio_array)
print("Audio saved as bark_output.wav") 