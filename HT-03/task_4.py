# 4. Write a script that combines three dictionaries by updating the first one.
# dict_1 = {'foo': 'bar', 'bar': 'buz'}
# dict_2 = {'dou': 'jones', 'USD': 36}
# dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {"foo": "bar", "bar": "buz"}
dict_2 = {"dou": "jones", "USD": 36}
dict_3 = {"AUD": 19.2, "name": "Tom"}

for dict in [dict_2, dict_3]:
    for key, value in dict.items():
        dict_1[key] = value

# Print result
print(f"New dictionaty: {dict_1}")
