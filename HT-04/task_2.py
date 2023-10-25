# Create a custom exception class called NegativeValueError. Write a Python program that takes an
# integer as input and raises the NegativeValueError if the input is negative. Handle this custom
# exception with a try/except block and display an error message.


class NegativeValueError(Exception):
    """Raise if int is negative"""


# Get user input
num = int(input("Write integer: "))

# Check if num is negative
try:
    if num < 0:
        raise NegativeValueError("Error: Number is negative!")
except NegativeValueError as e:
    print(e)
