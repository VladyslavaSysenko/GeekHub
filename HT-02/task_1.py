# 1. Write a script which accepts a sequence of comma-separated numbers from user and generate a
# list and a tuple with those numbers.

# Get user input
sequence = input("Write a sequence of comma-separated numbers:")

# Split string into list of numbers with type string
list_str = sequence.split(",")

# Change type of numbers from string to integer
list_int = [int(num) for num in list_str]

# Create tuple from list
tuple_int = tuple(list_int)

# Print both list and tuple
print(f"List: {list_int}")
print(f"Tuple: {tuple_int}")
