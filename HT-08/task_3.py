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


# Check if arguments are int
def is_int(*args) -> None:
    for value in args:
        if not isinstance(value, int):
            raise TypeError(f"'{type(value).__name__}' object cannot be interpreted as an integer")


# Check if step is not zero
def step_is_not_zero(step) -> None:
    if step == 0:
        raise ValueError("my_range() arg 3 must not be zero")


# Error if no arguments
def no_arguments(start) -> None:
    if start is None:
        raise TypeError("my_range expected at least 1 arguments, got 0")


def check_arguments(start, stop, step) -> tuple:
    no_arguments(start)
    # If only one argument than it is stop
    if stop is None:
        start, stop = 0, start
    is_int(start, stop, step)
    step_is_not_zero(step)
    return start, stop, step


def my_range(start=None, stop=None, step=1, /) -> Generator:
    # Check and assign arguments accordingly
    start, stop, step = check_arguments(start=start, stop=stop, step=step)
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

print(list(my_range(3)))
print(list(my_range(3, 8)))
print(list(my_range(3, 8, 2)))

print(list(my_range(0)))
print(list(my_range(5, 0)))
print(list(my_range(0, 5, -1)))
