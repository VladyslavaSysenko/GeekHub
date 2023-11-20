# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних.
#     - на старті додати можливість залогінитися або створити новго користувача (при створенні новго
#       користувача, перевіряється відповідність логіну і паролю мінімальним вимогам.)
#     - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме
#       розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що
#       підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
#       Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача (моделюємо
#       наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор


from tables import conn
from helper import get_atm_balance, get_change, get_sorted_atm_banknotes, get_user, update_banknotes
from validations import (
    has_needed_banknotes,
    is_enough_in_atm,
    is_enough_in_balance,
    is_existing_denomination,
    is_negative,
    is_positive,
)
from user_view import (
    deposit_withdraw,
    get_input_sum,
    get_login_or_register,
    get_user_action,
    login,
    register,
)
from staff_view import get_changed_denomination, get_staff_action


def ATM():
    """Main ATM function"""

    # Welcome user
    print("\nWelcome to the ATM", end="\n\n")
    # Get login or register action
    action = get_login_or_register()
    if not action:
        print("Wrong action number.", end="\n\n")
        return False

    # Log in user
    if action == "login":
        username = login()
        if not username:
            print("Invalid username and/or password.")
            return False
    # Register user
    else:
        while True:
            answer = register()
            # Incorrect values given
            if answer.get("message"):
                print(answer.get("message"))
                continue
            # User is registered
            else:
                username = answer.get("username")
                break

    # Get appropriate view
    if get_user(username=username)["is_staff"]:
        staff_view(username=username)
    else:
        user_view(username=username)
    # Close connection to database
    conn.close()


def user_view(username: str) -> None:
    while True:
        # Get needed action
        action = get_user_action()
        if not action:
            print("Wrong action number.", end="\n\n")

        # Do action
        match action:
            case "view_balance":
                balance = get_user(username=username)["balance"]
                print(f"Current balance: {balance}", end="\n\n")

            case "deposit":
                # Get money to deposit from user
                money = get_input_sum()
                # Check if correct input type
                if money is False:
                    print("Deposited amount of money must be integer.", end="\n\n")
                    continue
                # Check if positive amount
                if not is_positive(num=money):
                    print("Deposited amount of money must be bigger than 0.", end="\n\n")
                    continue
                # Check if change is needed
                change = get_change(needed_money=money)
                if change != 0:
                    money = money - change
                    print(f"Take your change: {change}")
                # Deposit money
                balance = deposit_withdraw(action=action, money=money, username=username)
                print(f"Deposited: {money}. Current balance: {balance}", end="\n\n")

            case "withdraw":
                # Get money to withdraw from user
                money = get_input_sum()
                # Check if correct input type
                if money is False:
                    print("Amount of money to withdraw must be integer.", end="\n\n")
                    continue
                # Check if positive amount
                if not is_positive(num=money):
                    print("Amount of money to withdraw must be bigger than 0.", end="\n\n")
                    continue
                # Ckeck if enough money in balance
                if not is_enough_in_balance(needed_money=money, username=username):
                    print("Not enough money to withdraw in balance.", end="\n\n")
                    continue
                # Check if enough money in atm
                if not is_enough_in_atm(needed_money=money):
                    print("Not enough money to withdraw in the ATM.", end="\n\n")
                    continue
                # Check if atm has needed banknotes
                res = has_needed_banknotes(needed_money=money)
                if res is not True:
                    print(
                        "Impossible to withraw with avaliable cash the ATM. "
                        f"Closest available amount: {res}",
                        end="\n\n",
                    )
                    continue
                # Withdraw money
                balance = deposit_withdraw(action=action, money=money, username=username)
                print(f"Withdrawn: {money}. Current balance: {balance}", end="\n\n")

            case "exit":
                print("You have successfully exited the ATM.")
                break


def staff_view(username: str) -> None:
    while True:
        # Get needed action
        action = get_staff_action()
        if not action:
            print("Wrong action number.", end="\n\n")

        # Do action
        match action:
            case "be_user":
                print("Entering user view.", end="\n\n")
                user_view(username=username)
                break

            case "view_atm_balance":
                balance = get_atm_balance()
                print(f"ATM balance: {balance}", end="\n\n")

            case "view_banknotes":
                banknotes = get_sorted_atm_banknotes()
                print("Denomination: amount")
                for banknote in banknotes:
                    print(f"{banknote['denomination']:<12}: {banknote['amount']}")
                # Add new line for nice visual
                print("")

            case "change_banknotes":
                # Get needed denomination and amount
                denomination, amount = get_changed_denomination()
                # Check if correct input type
                if denomination is False or amount is False:
                    print("Denomination and amount must be integers.", end="\n\n")
                    continue
                # Check if existing denomination
                if not is_existing_denomination(denomination=denomination):
                    print("Not existing denomination in the ATM.", end="\n\n")
                    continue
                # Check if not negative amount
                if is_negative(num=amount):
                    print("Amount of banknotes must be 0 or bigger.", end="\n\n")
                    continue
                # change amount of banknotes
                update_banknotes(denomination=denomination, amount=amount)
                print(f"Denomination: {denomination}, new amount: {amount}", end="\n\n")

            case "exit":
                print("You have successfully exited the ATM.")
                break


ATM()
