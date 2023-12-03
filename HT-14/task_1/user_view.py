from typing import Literal
from helper import Helper
from validations import Validation
import requests


class User:
    """
    Class for user view

    Attributes
    ---------
    db: DB

    Methods
    -------
    get_login_or_register()

    register()

    login()

    get_user_action()

    get_input_sum()

    deposit_withdraw(action: str, money: int, username: str, banknotes: list[dict] = None)

    Static methods
    -------------
    get_currency_rate()
    """

    def __init__(self, db) -> None:
        self.db = db

    def get_login_or_register(self) -> str | Literal[False]:
        """Get desired action from user if user needs login or register"""

        # Get user action
        num = input(
            "Available actions:\n\t1. Log in\n\t2. Register\nEnter number of the desired action:"
        )
        # Add new line for nice visual
        print("")
        # Return action or False
        return Validation(self.db).is_possible_auth_action(num)

    def register(self) -> str | Literal[False]:
        """Register user"""

        # Add new line for nice visual
        print("")
        # Get user username and password
        print("You have a 10% change to get 50 units!!!\nTo register, please type:")
        username = input("Username (must be 3 - 50 symbols long):")
        password = input(
            "Password (must be 8+ symbols long, have at least 1 number and 1 letter and not contain"
            " username):"
        )
        # Add new line for nice visual
        print("")

        # Check if valid input
        message = Validation(self.db).is_valid_register(username=username, password=password)
        if message is not True:
            return {"message": message}
        # Add user to database
        Helper(self.db).add_user(username=username, password=password)
        return {"username": username}

    def login(self) -> str | Literal[False]:
        """Log in user"""

        # Get user username and password
        username = input("Username:")
        password = input("Password:")
        # Add new line for nice visual
        print("")

        # Check input type
        if not (
            Validation().is_correct_type(username, str)
            and Validation().is_correct_type(password, str)
        ):
            return "Username and password must be strings."
        # Search for user with such username and password
        if Validation(self.db).is_existing_user(username=username, password=password):
            return username
        else:
            False

    def get_user_action(self) -> str | Literal[False]:
        """Get desired action from user"""

        # Get user action
        num = input(
            "Available actions:\n\t"
            "1. View card balance\n\t"
            "2. Deposit money\n\t"
            "3. Withdraw money\n\t"
            "4. View USD/UAH and EUR/UAH currency rate\n\t"
            "5. Exit\n"
            "Enter number of the desired action:"
        )
        # Add new line for nice visual
        print("")
        # Return action or False
        return Validation(self.db).is_possible_user_action(num)

    def get_input_sum(self) -> int | Literal[False]:
        """Get amount of money from user"""

        # Get amount of money
        money = input("Enter amount of money:")
        # Add new line for nice visual
        print("")
        # Check if input can be integer
        money = Validation().can_be_int(value=money)
        return money

    def deposit_withdraw(
        self, action: str, money: int, username: str, banknotes: list[dict] = None
    ) -> int:
        """Deposit or withdraw money. Action can be 'deposit' or 'withdraw'"""

        # Update balance
        balance = Helper(self.db).get_user(username=username)["balance"]
        new_balance = balance + money if action == "deposit" else balance - money
        Helper(self.db).update_balance(username=username, new_balance=new_balance)

        # Update banknotes
        if banknotes:
            Helper(self.db).delete_used_banknotes(used_banknotes=banknotes)

        # Write transaction
        if action == "withdraw":
            money = money * -1
        Helper(self.db).add_transaction(username=username, money=money)

        # Return balance
        return new_balance

    @staticmethod
    def get_currency_rate():
        """Get json USD/UAH and EUR/UAH currency rate from Privat Bank"""

        response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11")
        return response.json()
