# 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто
# функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з
# кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def shift_list(lst: list, shift: int):
    # Check type
    if not (isinstance(lst, list) and isinstance(shift, int)):
        return "List and/or shift number has wrong type"

    # Delete whole cycles of shift while can
    len_lst = len(lst)
    while shift > len_lst:
        shift = shift - len_lst
    # Move
    lst = lst[-shift:] + lst[:-shift]
    return lst


print(shift_list(lst="dd", shift=1))
print(shift_list(lst=[1, 2, 3, 4, 5], shift=1))
print(shift_list(lst=[1, 2, 3, 4, 5], shift=11))
print(shift_list(lst=[1, 2, 3, 4, 5], shift=-2))
