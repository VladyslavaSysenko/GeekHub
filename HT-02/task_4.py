# 4. Write a script which accepts a <number> from user and then <number> times asks user for string
# input. At the end script must print out result of concatenating all <number> strings.

# Get user input and covert to int type
number = int(input("Write a number of strings:"))

# Get all strings from user and concatenate them
result = ""
for i in range(0, number):
    result += input(f"String {i + 1}:")

# Print result
print(f"Concatenated string: {result}")
