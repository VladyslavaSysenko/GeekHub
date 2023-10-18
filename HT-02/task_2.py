# 2. Write a script which accepts two sequences of comma-separated colors from user. Then print out
# a set containing all the colors from color_list_1 which are not present in color_list_2.

# Get user input
sequence_1 = input("Write first sequence of comma-separated colors:")
sequence_2 = input("Write second sequence of comma-separated colors:")

# Split strings into list of colors and delete any repeats (turn list to set)
set_1 = set(sequence_1.split(","))
set_2 = set(sequence_2.split(","))

# Find colors from set 1 which are not present in set 2
difference = set_1 - set_2

# Print difference
print(f"Colors from first sequence which are not present in second sequence: {difference}")
