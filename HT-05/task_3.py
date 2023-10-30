# 3. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. Створiть просту умовну
# конструкцiю (звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися
# рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
#     Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#     x > y;       вiдповiдь - "х бiльше нiж у на z"
#     x < y;       вiдповiдь - "у бiльше нiж х на z"
#     x == y.      вiдповiдь - "х дорiвнює z"


def equality() -> str:
    # Get user input
    x = input("Enter X:")
    y = input("Enter Y:")
    # Check for correct input type
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return "Numbers must be int or float"
    # Compare numbers
    if x == y:
        return f"{x} equals {y}"
    if x > y:
        return f"{x} is more than {y} by {x - y}"
    if x < y:
        return f"{x} is less than {y} by {y - x}"


print(equality())
