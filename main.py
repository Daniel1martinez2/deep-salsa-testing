import time
from playsound import playsound
import threading

SONG = './data/sound/tracks/388.wav'
DATA = './data/txtfiles/388.txt'
PULSE = './data/sound/pulse/bellShort.wav'

def play1():
    playsound(PULSE)

threads = []

with open(DATA, 'r') as f:
    lines = f.readlines()
    lean = [int(x.replace(', bang;\n', '')) for x in lines]
    for i in lean:
        threads.append({
            "th": threading.Thread(target=play1),
            "pulse": i
        })

def play2():
    playsound(SONG)

t2 = threading.Thread(target=play2)
t2.start()

counter = 0
for thread in threads:
    time.sleep((thread['pulse'] - counter)/1000)
    counter = thread['pulse']
    print(thread)
    thread['th'].start()