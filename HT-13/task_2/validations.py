from typing import Literal
import re
from helper import Helper


class Validation:
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

    def is_existing_book_id(self, id: int) -> bool:
        """Check if existing book ID"""

        book = Helper(self.db).get_book(id=id)
        return bool(book)

    def is_available_book(self, id: int) -> bool:
        """Check if available book to reserve"""

        book = Helper(self.db).get_book(id=id)
        return bool(book["availability"])

    def is_users_book(self, username: str, book_id: int) -> bool:
        """Check if user's book reservation"""

        user_id = Helper(self.db).get_user(username=username)["user_id"]
        reservation = Helper(self.db).get_reservation(user_id=user_id, book_id=book_id)
        return bool(reservation)

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

        possible_actions = {
            "1": "see_books",
            "2": "see_user_books",
            "3": "reserve",
            "4": "return",
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
    def is_possible_staff_action(num: str) -> str | Literal[False]:
        """Check if action for staff with such number exists"""

        possible_actions = {
            "1": "be_user",
            "2": "see_books",
            "3": "see_user_books",
            "4": "add_book",
            "5": "delete_book",
            "6": "exit",
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
