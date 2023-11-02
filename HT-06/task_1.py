# 1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3
# значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.


def square(side: float) -> tuple | str:
    # Check input type
    if not isinstance(side, (int, float)):
        return "Side must be int or float"
    return (side * 4, side**2, side * 2 ** (1 / 2))


print(square("d"))
print(square(2))
print(square(3))
