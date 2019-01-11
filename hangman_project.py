import random

words = ["difficult", "locate", "field", "configure", "ambiguous", "versatile", "countermeasure",
         "capital", "signature", "_"]

random.shuffle(words)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lives = 8

active = True

if lives == 0:
    active = False
    print("Game Over!")

while active:
    print("filler")

# under construction
