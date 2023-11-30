import sqlite3


class DB:
    def __init__(self):
        # Connect to database
        self.conn = sqlite3.connect("library.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def create_tables(self) -> None:
        """Create all tables for db if not created"""

        # Create user table
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                is_staff INTEGER(1) NOT NULL default 0
            )
        """)

        # Create books table
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                availability INTEGER(1) NOT NULL default 1
            )
        """)

        # Create reservations table
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS reservations (
                reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id))
        """)
