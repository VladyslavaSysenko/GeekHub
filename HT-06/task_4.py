# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і
# вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.


def value_is_int(value) -> bool:
    return isinstance(value, int)


def start_less_than_end(start: int, end: int) -> bool:
    return start < end


def is_prime(num: int) -> bool:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    else:
        return True


def prime_list(start: int, end: int) -> list | str:
    # Check input type and value
    if not value_is_int(value=start) or not value_is_int(value=end):
        return "Numbers must be int"
    if not start_less_than_end(start=start, end=end):
        return "Start number must be bigger than end number"

    # Get prime numbers
    result = []
    for num in range(start, end + 1):
        if num > 1 and is_prime(num):
            result.append(num)
    return result


print(prime_list(1.1, 25))
print(prime_list(27, 25))
print(prime_list(-25, 25))
