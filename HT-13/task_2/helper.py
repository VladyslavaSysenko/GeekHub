from sqlite3 import Row
from typing import Literal


class Helper:
    def __init__(self, db=None) -> None:
        self.db = db

    def get_user(self, username: str) -> Row | None:
        """Get user from db"""
        self.db.cursor.execute(
            """
        SELECT user_id, username, is_staff FROM users WHERE username=?
        """,
            (username,),
        )
        return self.db.cursor.fetchone()

    def add_user(self, username: str, password: str) -> Literal[True]:
        """Add user to db"""

        self.db.cursor.execute(
            """
            INSERT INTO users(username, password) VALUES(?, ?)
            """,
            (username, password),
        )
        self.db.conn.commit()
        return True

    def add_book(self, title: str, author: str) -> Literal[True]:
        """Add book to db"""

        self.db.cursor.execute(
            """
            INSERT INTO books(title, author) VALUES(?, ?)
            """,
            (title, author),
        )
        self.db.conn.commit()
        return True

    def get_book(self, id: str) -> Row | None:
        """Get book from db"""
        self.db.cursor.execute(
            """
            SELECT * FROM books WHERE book_id=?
            """,
            (id,),
        )
        return self.db.cursor.fetchone()

    def delete_book(self, id: int) -> Literal[True]:
        """Delete book from db"""

        self.db.cursor.execute(
            """
            DELETE FROM books WHERE book_id=?
            """,
            (id,),
        )
        self.db.conn.commit()
        return True

    def update_book_availability(self, id: int, availability: bool) -> Literal[True]:
        """Update book availability"""

        self.db.cursor.execute(
            """
            UPDATE books SET availability = ? WHERE book_id = ?
            """,
            (int(availability), id),
        )
        self.db.conn.commit()
        return True

    def get_books(self) -> list[dict]:
        """Get all books info.
        Returns list of dicts {'book_id':int, 'title':str, 'author':str, 'availability':0|1}"""

        self.db.cursor.execute("""
            SELECT * FROM books
        """)
        return self.db.cursor.fetchall()

    def get_user_books(self, username: str) -> list[dict]:
        """Get all user reserved books info.
        Returns list of dicts {'book_id':int, 'title':str, 'author':str}"""

        user_id = self.get_user(username=username)["user_id"]
        self.db.cursor.execute(
            """
            SELECT books.book_id, books.title, books.author
            FROM books
            JOIN reservations ON books.book_id = reservations.book_id
            WHERE reservations.user_id = ?
            """,
            (user_id,),
        )
        return self.db.cursor.fetchall()

    def add_reservation(self, user_id: int, book_id: int) -> Literal[True]:
        """Add reservation to db"""

        self.db.cursor.execute(
            """
            INSERT INTO reservations(user_id, book_id) VALUES(?, ?)
            """,
            (user_id, book_id),
        )
        self.db.conn.commit()
        return True

    def get_reservation(self, user_id: int, book_id: int) -> Row | None:
        """Get reservation from db"""

        self.db.cursor.execute(
            """
            Select * FROM reservations WHERE user_id=? AND book_id=?
            """,
            (user_id, book_id),
        )
        return self.db.cursor.fetchone()

    def delete_reservation(self, user_id: int, book_id: int) -> Literal[True]:
        """Delete reservation from db"""

        self.db.cursor.execute(
            """
            DELETE FROM reservations WHERE user_id=? AND book_id=?
            """,
            (user_id, book_id),
        )
        self.db.conn.commit()
        return True
