# 2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь
# результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту
# ф-цiю, яка всередині викликає 3 попереднi, обробляє їх результат та також повертає результат своєї
# роботи. Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.


def check_type(num_1: float, num_2: float) -> bool:
    if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
        return True
    else:
        return False


def addition(num_1: float, num_2: float) -> int:
    return num_1 + num_2


def multiplication(num_1: float, num_2: float) -> int:
    return num_1 * num_2


def add_multiply(num_1: float, num_2: float) -> str:
    # Check type of variables
    if check_type(num_1=num_1, num_2=num_2):
        # Get addition and multiplication of two numbers
        add = addition(num_1=num_1, num_2=num_2)
        multipl = multiplication(num_1=num_1, num_2=num_2)
        # Return results
        return f"{num_1} + {num_2} = {add}\n{num_1} * {num_2} = {multipl}"
    else:
        return "Numbers must be int or float"


print(add_multiply(num_1=5, num_2="k"))
print(add_multiply(num_1=5.5, num_2=10))
