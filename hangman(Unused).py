"""
You many need these:
for i in range(len(list1)):
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
word = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dead_letters = []  # Letter choices that have been exhausted.
lives = 9  # This represents the limbs Hangman has left.
print("All letter choices must be capital")

for i in range(len(word)):
    if word[i] == "X":
        word.pop(i)
        word.insert(i, "*")

letters.remove(input("Choose a letter."))
