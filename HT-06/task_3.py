# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме
# True, якщо це число просте і False - якщо ні.


def is_int(num) -> bool:
    return isinstance(num, int)


def num_in_range(num: int) -> bool:
    return num > -1 and num < 1001


def is_prime(num: int) -> bool | str:
    # Check input type and if it is in range 0 - 1000
    if not is_int(num=num):
        return "Number must be int"
    if not num_in_range(num=num):
        return "Number must 0 - 1000"

    # Check half of numbers
    if num == 1:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True


print(is_prime("d"))
print(is_prime(1))
print(is_prime(4))
print(is_prime(5))
print(is_prime(10))
