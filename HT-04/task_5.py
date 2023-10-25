# Create a Python program that repeatedly prompts the user for a number until a valid integer is
# provided. Use a try/except block to handle any ValueError exceptions, and keep asking for input
# until a valid integer is entered. Display the final valid integer.


while True:
    # User input
    num = input("Write integer:")
    # Check if num is int
    try:
        num = int(num)
    except ValueError:
        print("Your input is not integer! Try again.")
    else:
        print("Your integer is", num)
        break
