# 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних
# букв та цифр, які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та
# букв (великих і малих). Реалізуйте обчислення за допомогою генератора.
#     Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі


from typing import Generator


def is_str(row) -> None:
    if not isinstance(row, str):
        raise TypeError("Row must have type str.")


def get_repeated(row: str) -> Generator:
    lower_row = row.lower()
    for elem in set(lower_row):
        if lower_row.count(elem) > 1:
            yield elem


def sum_repeated(row: str) -> int:
    is_str(row=row)
    return sum(1 for _ in get_repeated(row=row))


print(sum_repeated("abcde"))
print(sum_repeated("Indivisibilities"))
print(sum_repeated("aaA11BB"))
