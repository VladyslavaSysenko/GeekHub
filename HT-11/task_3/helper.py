from sqlite3 import Row
from typing import Literal
import random


class Helper:
    """
    Class for helping functions

    Attributes
    ---------
    db: DB, optional

    Methods
    -------
    get_user(username: str)

    update_balance(username: str, new_balance: int)

    add_transaction(username: str, money: int)

    add_user(username: str, password: str)

    get_atm_balance()

    get_atm_banknotes()

    get_sorted_atm_banknotes()

    get_needed_banknotes(needed_money: int)

    get_change(needed_money: int)

    update_banknotes(denomination: int, amount: int)

    """

    def __init__(self, db=None) -> None:
        self.db = db

    def get_user(self, username: str) -> Row | None:
        """Get user from db"""
        self.db.cursor.execute(
            """
        SELECT user_id, username, balance, is_staff FROM users WHERE username=?
        """,
            (username,),
        )
        return self.db.cursor.fetchone()

    def update_balance(self, username: str, new_balance: int) -> Literal[True]:
        """Update user balance"""

        self.db.cursor.execute(
            """
            UPDATE users SET balance = ? WHERE username = ?
            """,
            (new_balance, username),
        )
        self.db.conn.commit()
        return True

    def add_transaction(self, username: str, money: int) -> Literal[True]:
        """Add transaction to db. Positive money if deposit, negative if withdraw"""

        user_id = self.get_user(username=username)["user_id"]
        self.db.cursor.execute(
            """
            INSERT INTO transactions(user_id, amount) VALUES(?, ?)
            """,
            (user_id, money),
        )
        self.db.conn.commit()
        return True

    def add_user(self, username: str, password: str) -> Literal[True]:
        """Add user to db"""

        # Check if user gets bonus 50 units (10% chance)
        bonus = 50 if random.randint(0, 100) < 10 else 0
        self.db.cursor.execute(
            """
            INSERT INTO users(username, password, balance) VALUES(?, ?, ?)
            """,
            (username, password, bonus),
        )
        self.db.conn.commit()

        # Save transaction if has bonus
        if bonus:
            self.add_transaction(username=username, money=bonus)
        return True

    def get_atm_balance(self) -> int:
        """Get ATM balance"""
        self.db.cursor.execute("""
            SELECT denomination, amount FROM banknotes
        """)
        cash = self.db.cursor.fetchall()
        balance = 0
        for elem in cash:
            balance += elem["denomination"] * elem["amount"]
        return balance

    def get_atm_banknotes(self) -> list[dict]:
        """Get amount of ATM banknotes. Returns list of dicts {'denomination':int, 'amount':int}"""
        self.db.cursor.execute("""
            SELECT denomination, amount FROM banknotes
        """)
        return self.db.cursor.fetchall()

    def get_sorted_atm_banknotes(self) -> list[dict]:
        """Get amount of ATM banknotes sorted from biggest to smallest.
        Returns list of dicts {'denomination':int, 'amount':int}"""

        banknotes = self.get_atm_banknotes()
        return sorted(banknotes, key=lambda d: d["denomination"], reverse=True)

    def get_needed_banknotes(self, needed_money: int) -> dict:
        """Get atm banknotes for needed amount. Returns {'remaining':int, 'used_banknotes':list}"""

        banknotes = self.get_sorted_atm_banknotes()
        remaining_amount = needed_money
        used_banknotes = []

        for banknote in banknotes:
            denomination = banknote["denomination"]
            # Calculate the num of such banknotes that can be used and save it if less that available amount
            count = min(remaining_amount // denomination, banknote["amount"])

            if count > 0:
                # Update the remaining amount
                remaining_amount -= count * denomination

                # Store the count of the current denomination
                used_banknotes.append({"denomination": denomination, "amount": count})

            if remaining_amount == 0:
                break

        return {"remaining": remaining_amount, "used_banknotes": used_banknotes}

    def get_change(self, needed_money: int) -> int:
        """Get change for needed amount based on possible denominations"""

        banknotes = self.get_sorted_atm_banknotes()
        for banknote in banknotes:
            needed_money = needed_money % banknote["denomination"]

            if needed_money == 0:
                break

        return needed_money

    def update_banknotes(self, denomination: int, amount: int) -> Literal[True]:
        """Update denomination amount of banknotes"""
        self.db.cursor.execute(
            """
            UPDATE banknotes SET amount = ? WHERE denomination = ?
            """,
            (amount, denomination),
        )
        self.db.conn.commit()
        return True
