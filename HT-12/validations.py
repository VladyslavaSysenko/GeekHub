from typing import Literal
import re
from helper import Helper


class Validation:
    """
    Class for validations

    Attributes
    ---------
    db: DB, optional

    Methods
    -------
    is_existing_user(username: str, password: str)

    is_valid_register(username: str, password: str)

    is_enough_in_balance(needed_money: int, username: str)

    is_enough_in_atm(needed_money: int)

    is_existing_denomination(self, denomination: int)

    Static methods
    -------------
    is_possible_auth_action(num: str)

    is_possible_user_action(num: str)

    is_possible_staff_action(num: str)

    is_correct_type(value, type: type)

    can_be_int(value)

    is_positive(num: int)

    is_negative(num: int)

    """

    def __init__(self, db=None) -> None:
        self.db = db

    def is_existing_user(self, username: str, password: str) -> bool:
        """Check if user exists"""
        self.db.cursor.execute(
            """
            SELECT * FROM users WHERE username=? AND password=?
            """,
            (username, password),
        )
        return self.db.cursor.fetchone() is not None

    def is_valid_register(self, username: str, password: str) -> str | Literal[True]:
        # Username and password must be str
        if not (self.is_correct_type(username, str) and self.is_correct_type(password, str)):
            return "Username and password must be strings."

        # Username must be 3-50 symbols long
        if not 2 < len(username) < 51:
            return "Username must be 3 - 50 symbols long."

        # Username must be unique
        if Helper(db=self.db).get_user(username=username):
            return "Username is already taken. Please, choose another."

        # Password must be 8+ symbols long
        if len(password) < 8:
            return "Password must be 8+ symbols long."

        # Password must have 1+ number
        if not re.search(r"[0-9]+", password):
            return "Password must have at least 1 number."

        # Password must have 1+ letter
        if not re.search(r"[a-zA-Z]+", password):
            return "Password must have at least 1 letter."

        # Password cannot contain username
        if username in password:
            return "Password cannot contain username."

        return True

    def is_enough_in_balance(self, needed_money: int, username: str) -> bool:
        """Check if user has enough money"""

        balance = Helper(self.db).get_user(username=username)["balance"]
        return needed_money <= balance

    def is_enough_in_atm(self, needed_money: int) -> bool:
        """Check if atm has enough money"""

        return needed_money <= Helper(self.db).get_atm_balance()

    def is_existing_denomination(self, denomination: int) -> bool:
        """Check if available denomination in ATM"""
        banknotes = Helper(self.db).get_sorted_atm_banknotes()
        denominations = [banknote["denomination"] for banknote in banknotes]
        return denomination in denominations

    @staticmethod
    def is_possible_auth_action(num: str) -> str | Literal[False]:
        """Check if action with such number exists (1 or 2)"""

        possible_actions = {"1": "login", "2": "register"}
        # Action found
        try:
            action = possible_actions[num]
        # Action not found
        except KeyError:
            action = False
        return action

    @staticmethod
    def is_possible_user_action(num: str) -> str | Literal[False]:
        """Check if action for user with such number exists"""

        possible_actions = {"1": "view_balance", "2": "deposit", "3": "withdraw", "4": "exit"}
        # Action found
        try:
            action = possible_actions[num]
        # Action not found
        except KeyError:
            action = False
        return action

    @staticmethod
    def is_possible_staff_action(num: str) -> str | Literal[False]:
        """Check if action for staff with such number exists"""

        possible_actions = {
            "1": "be_user",
            "2": "view_atm_balance",
            "3": "view_banknotes",
            "4": "change_banknotes",
            "5": "exit",
        }
        # Action found
        try:
            action = possible_actions[num]
        # Action not found
        except KeyError:
            action = False
        return action

    @staticmethod
    def is_correct_type(value, type: type) -> bool:
        """Check if value has expected type"""
        return isinstance(value, type)

    @staticmethod
    def can_be_int(value) -> int | Literal[False]:
        """Check if value can be integer"""

        try:
            value = int(value)
        except ValueError:
            value = False
        return value

    @staticmethod
    def is_positive(num: int) -> bool:
        """Check if number is bigger than 0"""
        return num > 0

    @staticmethod
    def is_negative(num: int) -> bool:
        """Check if number is less than 0"""
        return num < 0
