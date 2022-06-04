import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

y, sr = librosa.load('./data/sound/tracks/310.wav')
D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
plt.figure()
librosa.display.specshow(S_db)
plt.colorbar()
# plt.show()
plt.savefig('figure.png')
# print(y, sr, D, S_db)