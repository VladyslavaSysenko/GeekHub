# 6. Write a script to check whether a value from user input is contained in a group of values.
# e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#  [1, 2, 'u', 'a', 4, True] --> 5 --> False

# Group of values
values = [1, 2, "u", "a", 4, True]

# Get user input
value = input("Write value to search for in the group '[1, 2, 'u', 'a', 4, True]':")

# Convert values to string
values = [str(val) for val in values]

# Check for value in values
if value in values:
    print("True")
else:
    print("False")
