# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

# Get user input and covert to int type
number = int(input("Write a number:"))

# Find sum of first <number> positive integers
total = 0
for i in range(1, number + 1):
    total += i

# Print result
print(f"Sum of first {number} positive integers = {total}")
