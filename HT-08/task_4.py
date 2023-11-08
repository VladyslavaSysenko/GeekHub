# 4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список,
# кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо
# було повернено останній елемент із послідовності - ітерація починається знову.
#    Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#    for elem in generator([1, 2, 3]):
#        print(elem)
#    1
#    2
#    3
#    1
#    2
#    3
#    1
#    .......

from typing import Generator


# Raise typeError if object is not iterable
def is_iterable(iter_row) -> None:
    iter(iter_row)


def infinite_generator(iter_row) -> Generator:
    # Check if row is iterable
    is_iterable(iter_row=iter_row)
    last_index = len(iter_row) - 1
    i = 0
    while True:
        yield iter_row[i]
        if i == last_index:
            i = 0
        else:
            i += 1


# for i in infinite_generator(123):
#     print(i)

# for i in infinite_generator("qwerty"):
#     print(i)

# for i in infinite_generator([1, 2, 3, 4, 5]):
#     print(i)
