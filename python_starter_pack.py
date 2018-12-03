"""
print("Hello World!")

# Apparently I'm going to slow, so i will speed up
# This is a comment
# This has no effect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work

print("Notice what is happening here.")
print()  # This creates a new line
print()  # Do you notice the underline here?

# Hover on top of it to see what is wrong.

# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)

# Intermediate Math
print("Figure this out.")
print(6 // 4)
print(12 // 3)
# Using "//" in math will ONLY give an integer, no decimals
print()
print(6 % 4)
print(5 % 3)
print(9 % 4)
print()
# Defining Variables
car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 2.55

print("I have a car called %s. It's pretty nice." % car_name)
print("It has %d cylinders, but gets %f MPG" % (car_cylinders, car_miles_per_gallon))

# Taking Input
name = input("What is your name?")
print("Hello %s" % name)

age = input("How old are you?")
print("%s" % age)
print()
# Recasting
real_age = input("How old are you again?")
hidden_age = real_age + str(5)
# The str() can convert any non-string line of code, such as an integer, into a string.
print(hidden_age)
print()
"""
# Multi-line Comments
"""
This is a multi-line comment anything in
between them is commented out.
"""
"""
# Defining Functions
def say_it():
    print("I'm back!")


say_it()
say_it()
say_it()
print()
# f(x) = 2x + 3


def f(x):
    print (2*x + 3)


f(10)
f(300)
f(5000)
# [**2] indicates raising a number by a power of 2.
# [**{1/2}] indicates a  square root.


def distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    print(dist)


# For [i] loops
for i in (1, 2, 3):
    say_it()


for i in range(5):  # Range(5) gives the numbers 0-4
    f(i)


for i in range(5):
    print(i**2)


# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as [a = a + 1].


print()
Hints for loops:
For loops - Use when you know EXACTLY how many iterations.
While loops - Use when you DON'T KNOW how many iterations.

# Control statements (if/else/elif statements)
sunny = True
if sunny:
    print("Go home")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(88)
print(your_grade)
print()

# Random Numbers
import random  # This should be on line 1
print(random.randint(0, 100))

# Equality statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)  # [!=] means NOT equal to

# a = 3 | [a] is set to 3.
# a == 3 | is [a] equal to 3? """
# O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O-----O #
"""
# Creating a list
fruit = ['apple', 'orange', 'peach', 'watermelon',
         'grape', 'pineapple', 'strawberry']

# Pulling items from a list
print(fruit[1])  # Remember to start counting from zero

# Getting the length of a list
print("This list contains %d entries." % len(fruit))  # len() is short for "length"

# Modifying Lists
fruit[4] = "banana"
print(fruit)

# Looping trough lists
for item in fruit:  # This goes through all items in a list once in order
    print(item)

# Pull the LAST item in a list
print("The last item in the list is %s" % fruit[len(fruit) - 1])

# chicken tastes bad
# ^ this is a lie ^
# ^ this is also a lie ^
# i liek chikin' 4 rael

food = ['beef', 'potatoes', 'bread', 'CHICKEN', 'oranges', 'corn',
        'fish', 'pasta', 'lettuce', 'crab', 'mushrooms', 'rice']

# Slicing lists
print(food[2:5])  # Excludes the last number.
print(food[3:4])
print(food[10:])  # Starts at index 10 and stops at the very end of the list.
print(food[:5])  # Goes up to (but not at) index 5.

# Adding entries to a list I (at the end)
food.append("cake")
food.append("pizza")
print(food)
# Everything is in the form Object.method(parameters)

# Adding entries to a list II (anywhere)
food.insert(2, "tomatoes")  # In here, the "2" in [2, tomatoes] represents position
print(food)

# Removing entries from a list I
food.remove("corn")
food.remove("lettuce")
print(food)

# Removing entries from a list II
# Sometimes, you don't know what is in a list, but you know
# You want to get rid of something from a list.
food.pop(0)  # [.pop] means "remove"
print(food)  # Notice that "beef" is no longer in the list as it was at index 0.

# Finding things in a list
print(food.index("CHICKEN"))  # Gives the index ID of the item

# AVOID [()] AT ALL COSTS WHEN MAKING A LIST"""

# Changing a string into a list
string1 = "turquoise"
list1 = list(string1)  # "split" into letters
print(list1)

# Hangman Hint
for i in range(len(list1)):
    if list1[i] == "u":  # "i" goes through all indices.
        list1.pop(i)
        list1.insert(i, "*")  # STOP BEING A BAD-MOUTH PYTHON!

# Changing a list into a string
print("".join(list1))  # revert back into a string


# Function Notes
# X ** 2 is the same as X to the second power.
# Y ** 1/2 is the same as taking Y's square root.
def pythagorean(a, b):
    return (a ** 2 + b ** 2) ** (1 / 2)


print(pythagorean(3, 4))
