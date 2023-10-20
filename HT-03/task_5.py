# 5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

# Hardcoded dictionary
dict = {1: 1, 2: 2, 3: "hi", 4: 1, 5: "hi", 6: 6}

# Add unique value to dict
new_dict = {}
for key, value in dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

# Print result
print(f"Dictionary with duplicate values: {dict}")
print(f"Dictionary without duplicate values: {new_dict}")
