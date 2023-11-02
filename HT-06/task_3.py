# 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме
# True, якщо це число просте і False - якщо ні.


def is_prime(num: int):
    # Check input type
    if not isinstance(num, int):
        return "Number must be int"
    elif num < 1 or num > 1001:
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
