# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і
# вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.


def check_type(start: int, end: int):
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Numbers must be int"
    return True


def check_value(start: int, end: int):
    if start >= end:
        return "Start number must be bigger than end number"
    return True


def prime_list(start: int, end: int):
    # Check input type and value
    type_message = check_type(start=start, end=end)
    value_message = check_value(start=start, end=end)
    if type_message is True:
        if value_message is True:
            # Get prime numbers
            result = []
            for num in range(start, end + 1):
                if num > 1:
                    for i in range(2, num // 2 + 1):
                        if num % i == 0:
                            break
                    else:
                        result.append(num)
            return result

        else:
            return value_message
    else:
        return type_message


print(prime_list(1.1, 25))
print(prime_list(27, 25))
print(prime_list(-25, 25))
