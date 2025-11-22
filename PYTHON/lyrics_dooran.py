 
import time
import sys

def time_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [ 
       "Sochunn ke milni te bolanga ki",
        "Teri taan gallaan ch shiri",
        "Vekhegi mainu te sochegi kya tu",
        "Mitti da banda main, tu taan pari",
        "Ishqe di galiyon ch khoia ayy dil ve",
        "Aas lagaaye ke jaaye tu mil ve",
        "Kol tere mainu aan de soni ",
        "karaan main kitne jatan",
        "Oh soni..?",
    ]
    delays = [2.0, 1.8, 2.1, 2.4, 1.7, 2.0, 2.3, 2.5, 0.0]
    
    time.sleep(1.5)
    for line, d in zip(lyrics, delays):
        time_lyric(line)
        time.sleep(d)

# Call the function to print the lyrics
print_lyrics()