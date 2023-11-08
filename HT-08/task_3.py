# 3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її
# можна було використати у вигляді:
#     for i in my_range(1, 10, 2):
#         print(i)
#     1
#     3
#     5
#     7
#     9
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
#    https://docs.python.org/3/library/stdtypes.html#range
#    P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)). Подивіться як веде
# себе стандартний range в таких випадках.


from typing import Generator


def is_int(*args) -> None:
    for value in args:
        if not isinstance(value, int):
            raise TypeError(f"'{type(value).__name__}' object cannot be interpreted as an integer")


def step_is_not_zero(step) -> None:
    if step == 0:
        raise ValueError("my_range() arg 3 must not be zero")


def assign_arguments(*args) -> tuple:
    len_args = len(args)
    if len_args == 0:
        raise TypeError("my_range expected at least 1 arguments, got 0")
    elif len_args > 3:
        raise TypeError(f"my_range expected at most 3 arguments, got {len_args}")
    # Correct amount of arguments
    else:
        is_int(*args)
        if len_args == 1:
            # start = 0, stop = arg, step = 1
            return 0, args[0], 1
        elif len_args == 2:
            # start = arg, stop = arg, step = 1
            return args[0], args[1], 1
        else:
            step_is_not_zero(args[2])
            # start = arg, stop = arg, step = arg
            return args[0], args[1], args[2]


def my_range(*args) -> Generator:
    # Assign arguments accordingly
    start, stop, step = assign_arguments(*args)
    # Calculate
    i = 0
    if step > 0:
        while True:
            res = start + step * i
            if res >= stop:
                break
            yield res
            i += 1
    else:
        while True:
            res = start + step * i
            if res <= stop:
                break
            yield res
            i += 1


# Errors
# print(list(my_range()))
# print(list(my_range(1, 3, 5, 7)))
# print(list(my_range(5.5)))
# print(list(my_range(1, 5, 0)))

print(my_range(3))
print(list(my_range(3)))
print(list(my_range(3, 8)))
print(list(my_range(3, 8, 2)))

print(list(my_range(0)))
print(list(my_range(5, 0)))
print(list(my_range(0, 5, -1)))
