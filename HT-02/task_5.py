# 5. Write a script which accepts decimal number from user and converts it to hexadecimal.

# Get user input and covert to int type
number = int(input("Write decimal number:"))

# Convert decimal to hexadecimal
hex_num = hex(number)

# Print result
print(f"Hexadecimal of {number} is {hex_num}")
