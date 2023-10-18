# 7. Write a script to concatenate all elements in a list into a string and print it. List must be
# include both strings and integers and must be hardcoded.

# List with strings and integers
lst = [1, 2, "j", 100, "apple", "QQ", -100]

# Convert all values of list to string
lst = [str(val) for val in lst]

# Concatenate all values
result = "".join(lst)

# Print result
print(f"Concatenated list: {result}")
