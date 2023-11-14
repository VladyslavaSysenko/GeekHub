# 3. Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію
#         транзакцій (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
#         (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання
#         нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні
#         - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже
#         закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути
#         повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)


import csv
import json
from typing import Literal


def ATM():
    """Main ATM function"""

    # Welcome user
    print("\nWelcome to the ATM", end="\n\n")

    # Log in user
    username = login()
    if not username:
        print("Invalid username and/or password.")
        return False

    while True:
        # Get needed action
        action = get_action()
        if not action:
            print("Wrong action number.", end="\n\n")

        # Do action
        match action:
            case "view_balance":
                balance = get_balance(username=username)
                print(f"Current balance: {balance}", end="\n\n")

            case "deposit":
                # Get money to deposit from user
                money = get_input_sum()
                # Wrong input type
                if money is False:
                    print("Deposited amount of money must be integer.", end="\n\n")
                    continue
                # Check if positive amount
                if not is_positive(num=money):
                    print("Deposited amount of money must be bigger than 0.", end="\n\n")
                    continue
                # Deposit money
                balance = deposit_withdraw(action=action, money=money, username=username)
                print(
                    f"Money has been successfully deposited. Current balance: {balance}", end="\n\n"
                )

            case "withdraw":
                # Get money to withdraw from user
                money = get_input_sum()
                # Wrong input type
                if money is False:
                    print("Amount of money to withdraw must be integer.", end="\n\n")
                    continue
                # Check if positive amount
                if not is_positive(num=money):
                    print("Amount of money to withdraw must be bigger than 0.", end="\n\n")
                    continue
                # Not enough money in balance
                if not is_enough_in_balance(username=username, needed_money=money):
                    print("Not enough money to withdraw in balance.", end="\n\n")
                    continue
                # Withdraw money
                balance = deposit_withdraw(action=action, money=money, username=username)
                print(
                    f"Money has been successfully withdrawn. Current balance: {balance}", end="\n\n"
                )

            case "exit":
                print("You have successfully exited the ATM.")
                break


def login() -> str | Literal[False]:
    """Log in user"""

    # Get user username and password
    username = input("Username:")
    password = input("Password:")
    # Add new line for nice visual
    print("")

    # Check input type
    if not (is_correct_type(username, str) and is_correct_type(password, str)):
        return "Username and password must be strings."

    # Search for user with such username and password
    with open("users.csv") as f:
        reader = csv.DictReader(f)
        # User found
        for user in reader:
            if user["username"] == username and user["password"] == password:
                return username
        # No user found
        return False


def get_action() -> str | Literal[False]:
    """Get desired action from user"""

    # Get user action
    num = input(
        "Available actions:\n\t"
        "1. View card balance\n\t"
        "2. Deposit money\n\t"
        "3. Withdraw money\n\t"
        "4. Exit\n"
        "Enter number of the desired action:"
    )
    # Add new line for nice visual
    print("")
    # Return action or False
    return is_possible_action(num)


def get_balance(username: str) -> int:
    """Get user balance"""

    with open(f"users_balance/{username}_balance.txt") as f:
        account_money = int(f.read())
    return account_money


def get_input_sum() -> int | Literal[False]:
    """Get amount of money from user"""

    # Get amount of money
    money = input("Enter amount of money:")
    # Check if input can be integer
    money = can_be_int(value=money)
    return money


def deposit_withdraw(action: str, money: int, username: str) -> int:
    """Deposit or withdraw money. Action can be 'deposit' or 'withdraw'"""

    # Update balance
    balance = get_balance(username=username)
    new_balance = balance + money if action == "deposit" else balance - money
    with open(f"users_balance/{username}_balance.txt", "w") as f:
        f.write(str(new_balance))

    # Write transaction
    with open(f"users_transactions/{username}_transactions.json", "a") as f:
        json.dump({action: money}, f)

    # Return balance
    return new_balance


def is_possible_action(num: str) -> str | Literal[False]:
    """Check if action with such number exists"""

    possible_actions = {"1": "view_balance", "2": "deposit", "3": "withdraw", "4": "exit"}
    # Action found
    try:
        action = possible_actions[num]
    # Action not found
    except KeyError:
        action = False
    return action


def is_correct_type(value, type: type) -> bool:
    """Check if value has expected type"""

    return isinstance(value, type)


def can_be_int(value) -> int | Literal[False]:
    """Check if value can be integer"""

    try:
        value = int(value)
    except ValueError:
        value = False
    return value


def is_positive(num: int) -> bool:
    """Check if number is bigger than 0"""

    return num > 0


def is_enough_in_balance(username: str, needed_money: int) -> bool:
    """Check if user has enough money"""

    balance = get_balance(username=username)
    return needed_money <= balance


ATM()
