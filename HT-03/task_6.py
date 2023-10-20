# 6. Write a script to get the maximum and minimum value in a dictionary.

# Hardcoded dictionary
dict = {"foo": "bar", "bar": -5.5, "dou": True, "USD": 36, "AUD": 19.2, "name": [1, 2, 2]}

# Get all values
values = [val for val in dict.values() if isinstance(val, (int, float))]

# Get minimum and maximum
min_v = min(values)
max_v = max(values)

# Print result
print(f"Minimum value: {min_v}")
print(f"Maximum value: {max_v}")
