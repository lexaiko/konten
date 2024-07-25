import time
import sys

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.15),
        ("About you?", 0.25),
        ("There was something 'bout you that now I can't remember", 0.08),
        ("It's the same damn thing that made my heart surrender", 0.09),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.09),
        ("I think about youuuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]

    delays = [0.2, 1.5, 1.5, 1.3, 3.0, 0.3, 0.4, 0.9, 0.5]

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        sing_lyric(lyric, delays[i], speed)

if __name__ == "__main__":
    sing_song()
