# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
# необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#        якщо silent == True - функція вертає False
#        якщо silent == False -породжується виключення LoginException (його також треба створити =))


class LoginException(Exception):
    """Raise if pair username and password is incorrect"""


def is_correct_type(value, type: type) -> bool:
    return isinstance(value, type)


def login(username: str, password: str, silent: bool = False) -> bool | str:
    # Check input type
    if not (
        is_correct_type(username, str)
        and is_correct_type(password, str)
        and is_correct_type(silent, bool)
    ):
        return "Username and password must be str, silent must be bool"

    # Hardcoded list of users
    users = [
        {"username": "Bob", "password": "123"},
        {"username": "Tom", "password": "456"},
        {"username": "Anne", "password": "789"},
        {"username": "Kate", "password": "qwerty"},
        {"username": "Sam", "password": "fFf"},
    ]

    # Correct login
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    # Incorrect login
    if silent:
        return False
    else:
        raise LoginException("Username or password is incorrect")


print(login(username="Bob", password=123))
print(login(username="Bob", password="123"))
print(login(username="Bob", password="123456", silent=True))
print(login(username="Bob", password="123456"))
