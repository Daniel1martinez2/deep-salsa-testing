from ast import Or
import time
from playsound import playsound as play_sound
import threading

user_input = input('Which song (311, 369, 377, 388): ')
VALUE =  int(user_input) if not user_input  == '' else 311
SONG = f'./data/sound/tracks/{VALUE}.wav'
DATA = f'./data/txtfiles/{VALUE}.txt'
PULSE = './data/sound/pulse/invaders.wav'

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
    counter = thread['pulse']
    print(f"{thread['pulse']} 💥💥💥")
    thread['th'].start()