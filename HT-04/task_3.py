# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120,
# raise a custom exception called InvalidAgeError. Handle the InvalidAgeError by displaying an
# appropriate error message.


class InvalidAgeError(Exception):
    """Raise if age is less than 18 or greater than 120"""


# Get user input
num = int(input("Write age: "))

# Check if num is negative
try:
    if num < 18 or num > 120:
        raise InvalidAgeError("Error: Age must me between 18 and 120")
except InvalidAgeError as e:
    print(e)
