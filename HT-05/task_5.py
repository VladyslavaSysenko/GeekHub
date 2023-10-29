# 5. Ну і традиційно - калькулятор: Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких
# операцiя, яку зробити! Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2;
# можна всі разом - типу 1 + 2).
# Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними
# значеннями на предмет помилок!


def calculator(num_1: float, op: str, num_2: float) -> str:
    result = ""
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
    except ZeroDivisionError:
        return "You cannot divide by zero!"
    else:
        return f"{num_1} {op} {num_2} = {result}"


print(calculator(-1.5, "+", 2))
print(calculator(-1.5, "-", 2))
print(calculator(-1, "*", 2))
print(calculator(-1.5, "**", 2))
print(calculator(-11.5, "/", 2))
print(calculator(-11.5, "//", 2))
print(calculator(-11, "%", 2))
print(calculator(-11, "%", 2))
print(calculator(-1, "//", 0))
