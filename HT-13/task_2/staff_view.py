from typing import Literal
from sqlalchemy import Row
from validations import Validation
from helper import Helper


class Staff:
    def __init__(self, db) -> None:
        self.db = db

    def get_staff_action(self) -> str | Literal[False]:
        """Get desired action from staff"""

        # Get user action
        num = input(
            "Available actions:\n\t"
            "1. Continue as user\n\t"
            "2. See all books\n\t"
            "3. See user reserved books\n\t"
            "4. Add a book\n\t"
            "5. Delete a book\n\t"
            "6. Exit\n"
            "Enter number of the desired action: "
        )
        # Add new line for nice visual
        print("")
        # Return action or False
        return Validation(self.db).is_possible_staff_action(num)

    def get_book_info(self) -> tuple[str, str]:
        """Get book information. Returns (title:str, author:str)"""

        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        # Add new line for nice visual
        print("")
        return title, author

    def get_book_id(self) -> int:
        """Get book id. Returns id:int"""

        id = input("Enter the id of the book: ")
        # Add new line for nice visual
        print("")
        # Check if input can be integer
        return Validation().can_be_int(value=id)

    def get_username(self) -> Row | None:
        """Get needed username from staff"""

        username = input("Enter needed username: ")
        # Add new line for nice visual
        print("")
        # Check if existing user
        user = Helper(db=self.db).get_user(username=username)
        return user["username"] if user else None
