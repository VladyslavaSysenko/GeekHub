# 4. Write a script which accepts a <number> from user and then <number> times asks user for string
# input. At the end script must print out result of concatenating all <number> strings.

# Get user input and covert to int type
number = int(input("Write a number of strings:"))

# Get all strings from user
list_strings = [input(f"String {i}:") for i in range(1, number + 1)]

# Concatenate all strings
result = "".join(list_strings)

# Print result
print(f"Concatenated string: {result}")
