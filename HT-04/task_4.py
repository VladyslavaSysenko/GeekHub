# Write a Python program that demonstrates exception chaining. Create a custom exception class
# called CustomError and another called SpecificError. In your program (could contain any logic you
# want), raise a SpecificError, and then catch it in a try/except block, re-raise it as a CustomError
# with the original exception as the cause. Display both the custom error message and the original
# exception message.

import random


class SpecificError(Exception):
    """Raise if user typed letter not from given"""


class CustomError(Exception):
    """Raise if SpecificError is raised"""


# User must guess right letter from letters Y, E, S
letters = ["Y", "E", "S"]
letter = random.choice(letters)

# Get user input
user_letter = input("See if you can beat random. \nChoose letter from letters Y, E, S: ")

# Check if input is correct
try:
    if user_letter not in letters:
        raise SpecificError("You must type only Y, E or S!")
except SpecificError as e:
    raise CustomError("You broke the game :(") from e
# Give the result
else:
    print("Correct!!!") if user_letter == letter else print("Wrong!!!")
