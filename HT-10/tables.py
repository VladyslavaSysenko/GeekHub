import sqlite3


# Connect to database
conn = sqlite3.connect("atm.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create user table
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        balance INTEGER NOT NULL default 0,
        is_staff INTEGER(1) NOT NULL default 0
    )
""")


# Create transactions table
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
""")

# Create banknotes table
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS banknotes (
        banknote_id INTEGER PRIMARY KEY AUTOINCREMENT,
        denomination INTEGER NOT NULL UNIQUE,
        amount INTEGER NOT NULL)
""")
