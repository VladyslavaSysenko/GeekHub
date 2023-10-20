# 7. Write a script which accepts a <number> from user and generates dictionary in range <number>
# where key is <number> and value is <number>*<number>
#     e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

# User input
num = int(input("Write a number:"))

# Create dict
dict = {}
for i in range(num + 1):
    dict[i] = i**2

# Print result
print(f"Dictionary: {dict}")
