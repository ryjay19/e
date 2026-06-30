import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyrics(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
    ("Padaba ta ka", 0.20),
    ("Daing ibang mumuyahon, kundi ikaaaa", 0.20),
    ("Mahal kita", 0.20),
    ("Walang ibang gugustuhin, kundi ikaw", 0.16),
    ("Mamahalin kita", 0.19),
    ("Hanggang sa ating pagtanda", 0.16),
    ("Walang ibang mamahalin, kundi ikaw", 0.15)
    ]


    delays = [0.5, 3.8, 7.5, 11.5, 15.2, 18.8, 22.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyrics, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()