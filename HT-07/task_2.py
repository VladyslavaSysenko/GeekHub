# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.


import re


class LoginException(Exception):
    """Raise if pair username and password is incorrect"""


def is_str(value) -> bool:
    return isinstance(value, str)


def is_valid_login(username: str, password: str):
    # Username and password must be str
    if not is_str(value=username) or not is_str(value=password):
        raise LoginException("Username and password must be str")

    # Username must be 3-50 symbols long
    if not 2 < len(username) < 51:
        raise LoginException("Username must be 3 - 50 symbols long")

    # Password must be 8+ symbols long and have 1+ number
    if len(password) < 8 or not re.search(r"\d", password):
        raise LoginException("Password must be 8+ symbols long and have 1+ number")

    # Password cannot contain username
    if username in password:
        raise LoginException("Password cannot contain username")

    return True


print(is_valid_login(username="Bob", password="zxcvbnm8"))
# print(is_valid_login(username="Bob", password=88888888))
# print(is_valid_login(username="Bo", password="zxcvbnm8"))
# print(is_valid_login(username="Bob", password="zx8"))
# print(is_valid_login(username="Bob", password="zxcvbnmi"))
# print(is_valid_login(username="Bob", password="Bob123465"))
