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
print("Look mommy! I learned some Python!")
print()
"""
# Multi-line Comments
"""
This is a multi-line comment anything in
between them is commented out.
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


# something

