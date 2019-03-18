import random

playing = True
word_bank = ["peel", "company", "wash", "flippant", "doubt",
             "cemetery", "stitch", "furniture", "sharp", "related"]

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

current_word = random.choice(word_bank)
correct_letters = list(current_word)
lives = 9  # Lose 1 life per incorrect guess. If this is 0, the game ends.
# print(current_word)
# print(correct_letters)
hidden_word = list("_" * len(current_word))


while playing:
    print(" ".join(hidden_word))
    # Ask for a letter
    guessed_letter = input("Choose a letter.")

    # Show the letter if it exists in the word
    for index in range(len(correct_letters)):
        if guessed_letter.lower() == correct_letters[index].lower():
            hidden_word[index] = correct_letters[index]

    if guessed_letter.lower() not in correct_letters and guessed_letter.upper() not in correct_letters:
        lives -= 1
        print("You have %d live(s) left" % lives)

    if "_" not in hidden_word:
        print("You win!")
        playing = False

    if lives == 0:
        print("You lost all your lives")
        playing = False
