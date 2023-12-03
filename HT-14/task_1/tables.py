import sqlite3


class DB:
    """
    Class for staff view

    Attributes
    ----------
    conn: Connection

    conn.row_factory: type[Row]

    cursor: Curson

    Methods
    -------
    create_tables()
    """

    def __init__(self):
        # Connect to database
        self.conn = sqlite3.connect("atm.db")
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
                balance INTEGER NOT NULL default 0,
                is_staff INTEGER(1) NOT NULL default 0
            )
        """)

        # Create transactions table
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        # Create banknotes table
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS banknotes (
                banknote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                denomination INTEGER NOT NULL UNIQUE,
                amount INTEGER NOT NULL)
        """)
