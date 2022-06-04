from colorama import Fore, Back, Style
import librosa
import time
from playsound import playsound as play_sound
import threading

user_input = input('Which song (310, 311, 312, 313): ')
VALUE =  int(user_input) if not user_input  == '' else 310
rate = librosa.get_samplerate("./data/sound/tracks/311.wav")
print(Fore.RED + f"The song rate is {rate}")
rate_value = '48K' if rate == 48000 else '44.1K'
SONG = f'./data/sound/tracks/{VALUE}.wav'
DATA = f'./data/txtfiles/{rate_value}/{VALUE}.txt'
PULSE = './data/sound/pulse/bellShort.wav'

def hit_pulse():
    play_sound(PULSE)

def play_song():
    play_sound(SONG)

threads = []
t2 = threading.Thread(target=play_song)

with open(DATA, 'r') as f:
    lines = f.readlines()
    lean = [int(x.replace(', bang;\n', '')) for x in lines]
    for i in lean:
        threads.append({
            "th": threading.Thread(target=hit_pulse),
            "pulse": i
        })

# Start the song
t2.start()
counter = 0

for thread in threads:
    time.sleep((thread['pulse'] - counter)/1000)
    print(Fore.GREEN + f"{thread['pulse']} 💥💥💥  {(thread['pulse'] - counter)} ")
    counter = thread['pulse']
    thread['th'].start()