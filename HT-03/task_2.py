# 2. Write a script to remove an empty elements from a list.
# Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list = [(), "hey", ("",), ("ma", "ke", "my"), [""], {}, ["d", "a", "y"], "", []]

# Remove empty elements
new_list = []
for ele in test_list:
    if ele:
        new_list.append(ele)

# Print result
print(f"Old list: {test_list}")
print(f"New list: {new_list}")
