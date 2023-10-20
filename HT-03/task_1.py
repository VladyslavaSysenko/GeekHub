# 1.Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of
# elements in the tuples must be different.

# Hardcoded list of tuples
list_tuples = [(True, False), (1, 2, 3), ("a", "b", "c", "d"), (-5, "hi", 25, True, 5555)]

# User input
replacement = input("Write a replacement value:")

# Create new list with changed last elements
new_list = []
for tpl in list_tuples:
    new_list.append(tpl[:-1] + (replacement,))

# Print list
print(f"Old list: {list_tuples}")
print(f"New list: {new_list}")
