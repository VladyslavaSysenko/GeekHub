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

    delete_used_banknotes(used_banknotes: list[dict])

    create_dict_of_banknotes(list_banknotes: list)

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
        """Get atm banknotes with smallest amount of banknotes using recursion with memoization

        Returns dict {"change": int, "used_banknotes": [{'denomination':int},'amount':int},...]

        If needed_money less than smallest available denomination:
        returns dict {"change": needed_money, "used_banknotes": []}
        """

        banknotes = self.get_sorted_atm_banknotes()
        len_banknotes = len(banknotes)

        # Helper function using recursion with memoization
        def helper(target: int, index: int = 0, memo: dict = {}):

            # Use info from memo if already calculated
            if (target, index) in memo:
                return memo[(target, index)]

            # Variables to track the minimum banknotes, remaining money and the corresponding combination
            min_banknotes = remaining = float("inf")
            best_combination = []

            # If the target amount is reached, return 0 banknotes
            if target == 0:
                return 0, 0, []

            # Invalid scenario if combination exceeded target
            if target < 0:
                return remaining, float("inf"), []
            # Invalid scenario if all denominations considered and combination not found
            if index == len_banknotes:
                return target, target, []

            # Iterate through the possible counts of the current denomination
            for count in range(banknotes[index]["amount"] + 1):
                remaining_target = target - count * banknotes[index]["denomination"]

                # Recursively call the helper function for the next index
                next_remaining, next_count, next_combination = helper(
                    remaining_target, index + 1, memo
                )

                # Update if the current combination has fewer banknotes than the current minimum
                if next_count + count < min_banknotes:
                    min_banknotes = next_count + count
                    remaining = next_remaining
                    # Save denomination if used
                    if count != 0:
                        best_combination = [
                            {"denomination": banknotes[index]["denomination"], "amount": count}
                        ] + next_combination
                    else:
                        best_combination = next_combination

            # Save calculated values
            memo[(target, index)] = remaining, min_banknotes, best_combination
            return remaining, min_banknotes, best_combination

        # Call the helper function to get the result
        remaining, count, used_banknotes = helper(target=needed_money)

        # Check if a valid combination was found
        if count == float("inf"):
            return {"change": needed_money, "used_banknotes": []}
        else:
            return {"change": remaining, "used_banknotes": used_banknotes}

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

    def delete_used_banknotes(self, used_banknotes: list[dict]) -> Literal[True]:
        """Update denomination amount of banknotes deleting used ones"""

        banknotes = self.get_sorted_atm_banknotes()

        # Create dictionary {denomination:amount,...}
        banknotes_dict = self.create_dict_of_banknotes(list_banknotes=banknotes)
        used_banknotes_dict = self.create_dict_of_banknotes(list_banknotes=used_banknotes)

        # Update all changed banknotes
        for denomination, amount in used_banknotes_dict.items():
            self.update_banknotes(
                denomination=denomination, amount=banknotes_dict[denomination] - amount
            )
        return True

    def create_dict_of_banknotes(self, list_banknotes: list) -> dict:
        """Create dictionary of banknotes {denomination:amount,...}
        from list of dicts {'denomination':int, 'amount':int}"""

        return {item["denomination"]: item["amount"] for item in list_banknotes}
