# 2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть
# фантазію). Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.


from typing import Literal
from helper import Helper
from staff_view import Staff
from tables import DB
from user_view import User
from validations import Validation


class Library:
    def __init__(self, db=DB()) -> None:
        self.db = db

    def work(self) -> Literal[False] | None:
        # Welcome user
        print("\nWelcome to the Library", end="\n\n")
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
                case "see_books":
                    # Get all books
                    books = Helper(self.db).get_books()
                    print("Library books:")
                    for book in books:
                        print(
                            f"ID: {book['book_id']}, Title: {book['title']}, "
                            f"Author: {book['author']}, "
                            f"Available: {'Yes' if book['availability'] else 'No'}"
                        )
                    # Add new line for nice visual
                    print("")

                case "see_user_books":
                    # Get user reserved books
                    books = Helper(self.db).get_user_books(username=self.username)
                    for book in books:
                        print(
                            f"ID: {book['book_id']}, Title: {book['title']}, "
                            f"Author: {book['author']}"
                        )
                    # Add new line for nice visual
                    print("")

                case "reserve":
                    print("Book reservation")
                    # Get book id to reserve
                    id = User(self.db).get_book_id()
                    # Check if correct input type
                    if id is False:
                        print("ID must be integer.", end="\n\n")
                        continue
                    # Check if existing id
                    if not Validation(self.db).is_existing_book_id(id=id):
                        print("Not existing ID in the Library.", end="\n\n")
                        continue
                    # Check if available to reservation
                    if not Validation(self.db).is_available_book(id=id):
                        print("Book is already reserved.", end="\n\n")
                        continue
                    # Reserve book
                    User(db=self.db).reserve_book(username=self.username, book_id=id)
                    print("The book is successfully reserved.", end="\n\n")

                case "return":
                    print("Book returning")
                    # Get book id to return
                    id = User(self.db).get_book_id()
                    # Check if correct input type
                    if id is False:
                        print("ID must be integer.", end="\n\n")
                        continue
                    # Check if existing id
                    if not Validation(self.db).is_existing_book_id(id=id):
                        print("Not existing ID in the Library.", end="\n\n")
                        continue
                    # Check if available for returning
                    if Validation(self.db).is_available_book(id=id):
                        print("Book is not reserved.", end="\n\n")
                        continue
                    # Check if user's reservation
                    if not Validation(self.db).is_users_book(username=self.username, book_id=id):
                        print("Book is not in your reservation.", end="\n\n")
                        continue
                    # Return book
                    User(db=self.db).return_book(username=self.username, book_id=id)
                    print("The book is successfully returned.", end="\n\n")

                case "exit":
                    print("You have successfully exited the Library.")
                    break


class StaffView:
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

                case "see_books":
                    # Get all books
                    books = Helper(self.db).get_books()
                    print("Library books:")
                    for book in books:
                        print(
                            f"ID: {book['book_id']}, Title: {book['title']}, "
                            f"Author: {book['author']}, "
                            f"Available: {'Yes' if book['availability'] else 'No'}"
                        )
                    # Add new line for nice visual
                    print("")

                case "see_user_books":
                    # Get wanted username
                    wanted_username = Staff(self.db).get_username()
                    # Check if user exists
                    if not wanted_username:
                        print("No user with such username", end="\n\n")
                        continue
                    # Get user reserved books
                    books = Helper(self.db).get_user_books(username=wanted_username)
                    if books != []:
                        print(f"{wanted_username}'s reservations:")
                        for book in books:
                            print(
                                f"ID: {book['book_id']}, Title: {book['title']}, "
                                f"Author: {book['author']}"
                            )
                    else:
                        print(f"{wanted_username} has no reservations.")
                    # Add new line for nice visual
                    print("")

                case "add_book":
                    # Get book info to add
                    title, author = Staff(self.db).get_book_info()
                    # Add book to db
                    Helper(self.db).add_book(title=title, author=author)
                    print("The book is successfully added.", end="\n\n")

                case "delete_book":
                    # Get book id to delete
                    id = Staff(self.db).get_book_id()
                    # Check if correct input type
                    if id is False:
                        print("ID must be integer.", end="\n\n")
                        continue
                    # Check if existing id
                    if not Validation(self.db).is_existing_book_id(id=id):
                        print("Not existing ID in the Library.", end="\n\n")
                        continue
                    # Delete book from db
                    Helper(self.db).delete_book(id=id)
                    print("The book is successfully deleted.", end="\n\n")

                case "exit":
                    print("You have successfully exited the Library.")
                    break


Library().work()
