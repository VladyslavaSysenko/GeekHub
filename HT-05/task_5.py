# 5. Ну і традиційно - калькулятор: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких
# операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2;
# можна всі разом - типу 1 + 2).
# Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними
# значеннями на предмет помилок!


def calculator() -> str:
    # Get user input
    num_1 = input("Enter the first number:")
    op = input("Enter operand:")
    num_2 = input("Enter the second number:")
    # Check for correct input type
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        return "Numbers must be int or float"
    # Calculate
    result = 0
    try:
        match op:
            case "+":
                result = num_1 + num_2
            case "-":
                result = num_1 - num_2
            case "*":
                result = num_1 * num_2
            case "**":
                result = num_1**num_2
            case "/":
                result = num_1 / num_2
            case "%":
                result = num_1 % num_2
            case "//":
                result = num_1 // num_2
            # Error if wrong operand
            case _:
                return "Operand must be +, -, *, **, /, // or %"
    except ZeroDivisionError:
        return "You cannot divide by zero!"
    else:
        return f"{num_1} {op} {num_2} = {result}"


print(calculator())
