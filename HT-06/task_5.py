# 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не
# перевищують його.


def fibonacci(num: int):
    # Check type
    if not (isinstance(num, int) and num >= 0):
        return "Number must be positive"

    # Return 0 if num = 0
    if num == 0:
        return [0]
    # Calculate fibonacci
    result = [0, 1]
    for i in range(2, num + 1):
        # Add the previous two numbers to get the next number in the sequence
        next_number = result[i - 1] + result[i - 2]
        # Stop if next number bigger than given
        if next_number > num:
            break
        result.append(next_number)
    return result


print(fibonacci("l"))
print(fibonacci(0))
print(fibonacci(20))
print(fibonacci(10000))
