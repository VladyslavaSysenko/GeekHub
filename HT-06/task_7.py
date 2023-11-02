# 7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових
# елементів у ньомy і виводить результат. Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
#     1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"


# First way ignored type so 1 and "1" are the same
def similar_1(lst: list) -> str:
    # Check type
    if not (isinstance(lst, list)):
        return "List has wrong type"

    # Turn values to str
    lst = [str(v) for v in lst]
    set_val = set(lst)
    # Calculate amount
    result = {}
    for val in set_val:
        amount = lst.count(val)
        result.update({val: amount})
    # Turn results to needed format
    answer = [f"{x} -> {y}" for x, y in result.items()]
    return ", ".join(answer)


# In second way 1 and "1" are not the same
def similar_2(lst: list) -> str:
    # Check type
    if not (isinstance(lst, list)):
        return "List has wrong type"

    # Calculate amount
    result = []
    while len(lst) > 0:
        # Get first element of list
        variable = lst.pop(0)
        amount = 1
        # Check for duplicates
        for elem in lst:
            if isinstance(variable, type(elem)) and variable == elem:
                lst.remove(elem)
                amount += 1
        # Explicitly define strings
        if isinstance(variable, str):
            result.append(f"'{variable}' -> {amount}")
        else:
            result.append(f"{variable} -> {amount}")
    return ", ".join(result)


print(similar_1("d"))
print(similar_1([1, "1", "foo", [1, 2, [1, 3]], True, "foo", 1, [1, 2, [1, 3]], [1, 2, [1, 3]]]))

print(similar_2("d"))
print(similar_2([1, "1", "foo", [1, 2, [1, 3]], True, "foo", 1, [1, 2, [1, 3]], [1, 2, [1, "3"]]]))
