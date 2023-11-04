# 3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї
#       функції) - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці
#       дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)


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


# Task 3

users = [
    ("Bob", "zxcvbnm8"),
    ("Bob", 88888888),
    ("Bo", "zxcvbnm8"),
    ("Bob", "zx8"),
    ("Bob", "zxcvbnmi"),
    ("Bob", "Bob123465"),
]


def login_info(users: list) -> None:
    for user in users:
        username, password = user[0], user[1]
        print(f"Name: {username}", f"Password: {password}", sep="\n")
        try:
            is_valid_login(username=username, password=password)
        except LoginException as e:
            print(f"Status: {e}", "-" * 60, sep="\n")
        else:
            print("Status: OK", "-" * 60, sep="\n")


login_info(users=users)
