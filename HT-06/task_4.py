# 4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і
# вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
# введених даних та у випадку невідповідності - виведіть повідомлення.


def prime_list(start: int, end: int):
    # Check input type
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Numbers must be int"
    elif start >= end:
        return "Start number must be bigger than end number"

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


print(prime_list(1.1, 25))
print(prime_list(27, 25))
print(prime_list(-25, 25))
