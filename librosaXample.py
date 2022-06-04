import librosa

rate = librosa.get_samplerate("./data/sound/tracks/313.wav")
print(rate)