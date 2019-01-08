import random
print()
guess = input("Select an integer between 0 and 10.")
random_integer = (random.randint(0, 10))
print(random_integer)

if int(guess) == int(random_integer):
    print("You win!")
else:
    print("Try again.")
