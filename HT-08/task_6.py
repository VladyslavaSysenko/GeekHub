# 6. Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.


from typing import Generator


def is_str(row) -> None:
    if not isinstance(row, str):
        raise TypeError("Row must have type str.")


def word_len(row: str) -> Generator:
    for word in row.split():
        yield len(word)


def len_shortest(row: str) -> int:
    # Check argument type
    is_str(row=row)
    # Return length of shortest word
    return min(word_len(row))


# print(len_shortest(1111))
print(len_shortest("111"))
print(len_shortest("11111 sfdfdf dfdfdfdfdfdfdfd"))
