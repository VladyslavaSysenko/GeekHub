# 4. Write a script that combines three dictionaries by updating the first one.
# dict_1 = {'foo': 'bar', 'bar': 'buz'}
# dict_2 = {'dou': 'jones', 'USD': 36}
# dict_3 = {'AUD': 19.2, 'name': 'Tom'}

dict_1 = {"foo": "bar", "bar": "buz"}
dict_2 = {"dou": "jones", "USD": 36}
dict_3 = {"AUD": 19.2, "name": "Tom"}

for dict in [dict_2, dict_3]:
    dict_1.update(dict)

# Print result
print(f"New dictionary: {dict_1}")
