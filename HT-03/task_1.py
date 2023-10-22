# 1.Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of
# elements in the tuples must be different.

# Hardcoded list of tuples
list_tuples = [(1, 5, True), ("aaa", 2), (0,), ()]

# User input
replacement = input("Write a replacement value:")

# Create new list with changed last elements
new_list = []
for tpl in list_tuples:
    if tpl:
        new_list.append(tpl[:-1] + (replacement,))
    else:
        new_list.append(tpl)

# Print list
print(f"Old list: {list_tuples}")
print(f"New list: {new_list}")
