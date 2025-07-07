import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

model = ChatterboxTTS.from_pretrained(device="cpu")  # Use "cuda" if you have a GPU

text = "How many liters of water should a 5 foot 2 inch woman drink per day?"
AUDIO_PROMPT_PATH = "reference.wav"  # Path to your reference audio
wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
ta.save("test-tts-cloned.wav", wav, model.sr)
print("Cloned voice audio saved as test-tts-cloned.wav") 