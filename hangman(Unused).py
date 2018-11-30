"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You many need these:
for i in range(len(list1)):
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
word = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dead_letters = []  # Letter choices that have been exhausted.
lives = 9  # This represents how many limbs Hangman has left.
print("All letter choices must be capital")
while lives > 0:
    print(dead_letters)
    active_choice = input("Choose a letter.")
    for i in range(len(word)):
        if word[i] == active_choice:
            word.pop(i)
            word.insert(i, "#")
            print("The letter (%s) is part of the word!" % active_choice)
            print(word)
        else:
            lives -= 1
            print("The letter (%s) is not in the word. Lives remaining: %d" % (active_choice, lives))
    letters.remove(active_choice)
    dead_letters.append(active_choice)
    print("Used letter(s): %s" % dead_letters)

print("filler")
