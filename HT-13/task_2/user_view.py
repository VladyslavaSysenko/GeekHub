from typing import Literal
from helper import Helper
from validations import Validation


class User:
    def __init__(self, db) -> None:
        self.db = db

    def get_login_or_register(self) -> str | Literal[False]:
        """Get desired action from user if user needs login or register"""

        # Get user action
        num = input(
            "Available actions:\n\t1. Log in\n\t2. Register\nEnter number of the desired action: "
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
        username = input("Username (must be 3 - 50 symbols long): ")
        password = input(
            "Password (must be 8+ symbols long, have at least 1 number and 1 letter and not contain"
            " username): "
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
            "1. See all books\n\t"
            "2. See my reserved books\n\t"
            "3. Reserve a book\n\t"
            "4. Return a book\n\t"
            "5. Exit\n"
            "Enter number of the desired action: "
        )
        # Add new line for nice visual
        print("")
        # Return action or False
        return Validation(self.db).is_possible_user_action(num)

    def get_book_id(self) -> int:
        """Get book id. Returns id:int"""

        id = input("Enter the id of the book: ")
        # Add new line for nice visual
        print("")
        # Check if input can be integer
        return Validation().can_be_int(value=id)

    def reserve_book(self, username: str, book_id: int) -> Literal[True]:
        """Reserve book"""

        user_id = Helper(self.db).get_user(username=username)["user_id"]

        Helper(self.db).update_book_availability(id=book_id, availability=False)
        Helper(self.db).add_reservation(user_id=user_id, book_id=book_id)
        return True

    def return_book(self, username: str, book_id: int) -> Literal[True]:
        """Return book"""

        user_id = Helper(self.db).get_user(username=username)["user_id"]

        Helper(self.db).update_book_availability(id=book_id, availability=True)
        Helper(self.db).delete_reservation(user_id=user_id, book_id=book_id)
        return True
