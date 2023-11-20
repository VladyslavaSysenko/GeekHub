from tables import cursor, conn
from sqlite3 import Row
from typing import Literal


def get_user(username: str) -> Row:
    """Get user from db"""
    cursor.execute(
        """
    SELECT user_id, username, balance, is_staff FROM users WHERE username=?
    """,
        (username,),
    )
    return cursor.fetchone()


def update_balance(username: str, new_balance: int) -> Literal[True]:
    """Update user balance"""

    cursor.execute(
        """
        UPDATE users SET balance = ? WHERE username = ?
        """,
        (new_balance, username),
    )
    conn.commit()
    return True


def add_transaction(username: str, money: int) -> Literal[True]:
    """Add transaction to db. Positive money if deposit, negative if withdraw"""

    user_id = get_user(username=username)["user_id"]
    cursor.execute(
        """
        INSERT INTO transactions(user_id, amount) VALUES(?, ?)
        """,
        (user_id, money),
    )
    conn.commit()
    return True


def add_user(username: str, password: str) -> Literal[True]:
    """Add user to db"""

    cursor.execute(
        """
        INSERT INTO users(username, password) VALUES(?, ?)
        """,
        (username, password),
    )
    conn.commit()
    return True


def get_atm_balance() -> int:
    """Get ATM balance"""
    cursor.execute("""
        SELECT denomination, amount FROM banknotes
    """)
    cash = cursor.fetchall()
    balance = 0
    for elem in cash:
        balance += elem["denomination"] * elem["amount"]
    return balance


def get_atm_banknotes() -> list[dict]:
    """Get amount of ATM banknotes. Returns list of dicts {'denomination':int, 'amount':int}"""
    cursor.execute("""
        SELECT denomination, amount FROM banknotes
    """)
    return cursor.fetchall()


def get_sorted_atm_banknotes() -> list[dict]:
    """Get amount of ATM banknotes sorted from biggest to smallest.
    Returns list of dicts {'denomination':int, 'amount':int}"""

    banknotes = get_atm_banknotes()
    return sorted(banknotes, key=lambda d: d["denomination"], reverse=True)


def get_needed_banknotes(needed_money: int) -> dict:
    """Get atm banknotes for needed amount. Returns {'remaining':int, 'used_banknotes':list}"""

    banknotes = get_sorted_atm_banknotes()
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


def get_change(needed_money: int) -> int:
    """Get change for needed amount based on possible denominations"""

    banknotes = get_sorted_atm_banknotes()
    for banknote in banknotes:
        needed_money = needed_money % banknote["denomination"]

        if needed_money == 0:
            break

    return needed_money


def update_banknotes(denomination: int, amount: int) -> Literal[True]:
    """Update denomination amount of banknotes"""
    cursor.execute(
        """
        UPDATE banknotes SET amount = ? WHERE denomination = ?
        """,
        (amount, denomination),
    )
    conn.commit()
    return True
