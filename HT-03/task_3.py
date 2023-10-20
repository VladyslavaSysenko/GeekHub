# 3. Write a script to concatenate following dictionaries to create a new one.
# dict_1 = {'foo': 'bar', 'bar': 'buz'}
# dict_2 = {'dou': 'jones', 'USD': 36}
# dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {"foo": "bar", "bar": "buz"}
dict_2 = {"dou": "jones", "USD": 36}
dict_3 = {"AUD": 19.2, "name": "Tom"}

new_dict = {}

for dict in [dict_1, dict_2, dict_3]:
    for key, value in dict.items():
        new_dict[key] = value

# Print result
print(f"New dictionary: {new_dict}")
