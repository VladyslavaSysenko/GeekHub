# Банкомат 5.0
# 1. Додайте до банкомату меню отримання поточного курсу валют за допомогою requests (можна
# використати відкрите API ПриватБанку)


from typing import Literal
from helper import Helper
from staff_view import Staff
from tables import DB
from user_view import User
from validations import Validation


class ATM:
    """
    Class for Main ATM

    Attributes
    ---------
    db: DB, optional

    Methods
    -------
    work()
    """

    def __init__(self, db=DB()) -> None:
        self.db = db

    def work(self) -> Literal[False] | None:
        # Welcome user
        print("\nWelcome to the ATM", end="\n\n")
        # Get login or register action
        action = User(self.db).get_login_or_register()
        if not action:
            print("Wrong action number.", end="\n\n")
            return False

        # Create tables
        self.db.create_tables()

        # Log in user
        if action == "login":
            username = User(self.db).login()
            if not username:
                print("Invalid username and/or password.")
                return False
        # Register user
        else:
            while True:
                answer = User(self.db).register()
                # Incorrect values given
                if answer.get("message"):
                    print(answer.get("message"))
                    continue
                # User is registered
                else:
                    username = answer.get("username")
                    break

        # Get appropriate view
        if Helper(self.db).get_user(username=username)["is_staff"]:
            StaffView(username=username, db=self.db).load()
        else:
            UserView(username=username, db=self.db).load()
        # Close connection to database
        self.db.conn.close()


class UserView:
    """
    Class for Main User View

    Attributes
    ---------
    username: str
    db: DB

    Methods
    -------
    load()
    """

    def __init__(self, username: str, db) -> None:
        self.username = username
        self.db = db

    def load(self) -> None:
        while True:
            # Get needed action
            action = User(self.db).get_user_action()
            if not action:
                print("Wrong action number.", end="\n\n")

            # Do action
            match action:
                case "view_balance":
                    balance = Helper(self.db).get_user(username=self.username)["balance"]
                    print(f"Current balance: {balance}", end="\n\n")

                case "deposit":
                    # Get money to deposit from user
                    money = User(self.db).get_input_sum()
                    # Check if correct input type
                    if money is False:
                        print("Deposited amount of money must be integer.", end="\n\n")
                        continue
                    # Check if positive amount
                    if not Validation(self.db).is_positive(num=money):
                        print("Deposited amount of money must be bigger than 0.", end="\n\n")
                        continue
                    # Check if change is needed
                    change = Helper(self.db).get_change(needed_money=money)
                    if change != 0:
                        money = money - change
                        print(f"Take your change: {change}")
                    # Deposit money
                    balance = User(self.db).deposit_withdraw(
                        action=action, money=money, username=self.username
                    )
                    print(f"Deposited: {money}. Current balance: {balance}", end="\n\n")

                case "withdraw":
                    # Get money to withdraw from user
                    money = User(self.db).get_input_sum()
                    # Check if correct input type
                    if money is False:
                        print("Amount of money to withdraw must be integer.", end="\n\n")
                        continue
                    # Check if positive amount
                    if not Validation(self.db).is_positive(num=money):
                        print("Amount of money to withdraw must be bigger than 0.", end="\n\n")
                        continue
                    # Ckeck if enough money in balance
                    if not Validation(self.db).is_enough_in_balance(
                        needed_money=money, username=self.username
                    ):
                        print("Not enough money to withdraw in balance.", end="\n\n")
                        continue
                    # Check if enough money in atm
                    if not Validation(self.db).is_enough_in_atm(needed_money=money):
                        print("Not enough money to withdraw in the ATM.", end="\n\n")
                        continue
                    # Check if atm has needed banknotes and get them
                    res = Helper(self.db).get_needed_banknotes(needed_money=money)
                    if res["change"] != 0:
                        print("Impossible to withraw with avaliable cash the ATM.", end=" ")
                        if res["used_banknotes"]:
                            print(f"Closest available amount: {money - res['change']}")
                        else:
                            print("Smaller than avaliable denominations.")
                        print("")
                        continue
                    # Withdraw money
                    balance = User(self.db).deposit_withdraw(
                        action=action,
                        money=money,
                        username=self.username,
                        banknotes=res["used_banknotes"],
                    )
                    print(f"Withdrawn: {money}. Current balance: {balance}")
                    print("Your banknotes:")
                    for banknote in res["used_banknotes"]:
                        print(f"{banknote['denomination']:<5}: {banknote['amount']}")
                    print("")

                case "get_currency_rate":
                    rates = User(self.db).get_currency_rate()
                    for pair in rates:
                        print(f'{pair["ccy"]}/UAH')
                        print(f"Buying rate:  {pair['buy']}")
                        print(f"Selling rate: {pair['sale']}", end="\n\n")

                case "exit":
                    print("You have successfully exited the ATM.")
                    break


class StaffView:
    """
    Class for Main Staff View

    Attributes
    ---------
    username: str
    db: DB

    Methods
    -------
    load()
    """

    def __init__(self, username: str, db) -> None:
        self.username = username
        self.db = db

    def load(self) -> None:
        while True:
            # Get needed action
            action = Staff(self.db).get_staff_action()
            if not action:
                print("Wrong action number.", end="\n\n")

            # Do action
            match action:
                case "be_user":
                    print("Entering user view.", end="\n\n")
                    UserView(username=self.username, db=self.db).load()
                    break

                case "view_atm_balance":
                    balance = Helper(self.db).get_atm_balance()
                    print(f"ATM balance: {balance}", end="\n\n")

                case "view_banknotes":
                    banknotes = Helper(self.db).get_sorted_atm_banknotes()
                    print("Denomination: amount")
                    for banknote in banknotes:
                        print(f"{banknote['denomination']:<12}: {banknote['amount']}")
                    # Add new line for nice visual
                    print("")

                case "change_banknotes":
                    # Get needed denomination and amount
                    denomination, amount = Staff(self.db).get_changed_denomination()
                    # Check if correct input type
                    if denomination is False or amount is False:
                        print("Denomination and amount must be integers.", end="\n\n")
                        continue
                    # Check if existing denomination
                    if not Validation(self.db).is_existing_denomination(denomination=denomination):
                        print("Not existing denomination in the ATM.", end="\n\n")
                        continue
                    # Check if not negative amount
                    if Validation(self.db).is_negative(num=amount):
                        print("Amount of banknotes must be 0 or bigger.", end="\n\n")
                        continue
                    # change amount of banknotes
                    Helper(self.db).update_banknotes(denomination=denomination, amount=amount)
                    print(f"Denomination: {denomination}, new amount: {amount}", end="\n\n")

                case "exit":
                    print("You have successfully exited the ATM.")
                    break


ATM().work()
