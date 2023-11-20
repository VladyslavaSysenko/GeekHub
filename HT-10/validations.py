from typing import Literal
from tables import cursor
import re
from helper import get_user, get_atm_balance, get_needed_banknotes, get_sorted_atm_banknotes


def is_existing_user(username: str, password: str) -> bool:
    """Check if user exists"""
    cursor.execute(
        """
        SELECT * FROM users WHERE username=? AND password=?
        """,
        (username, password),
    )
    return cursor.fetchone() is not None


def is_possible_auth_action(num: str) -> str | Literal[False]:
    """Check if action with such number exists (1 or 2)"""

    possible_actions = {"1": "login", "2": "register"}
    # Action found
    try:
        action = possible_actions[num]
    # Action not found
    except KeyError:
        action = False
    return action


def is_valid_register(username: str, password: str) -> str | Literal[True]:
    # Username and password must be str
    if not (is_correct_type(username, str) and is_correct_type(password, str)):
        return "Username and password must be strings."

    # Username must be 3-50 symbols long
    if not 2 < len(username) < 51:
        return "Username must be 3 - 50 symbols long."

    # Password must be 8+ symbols long
    if len(password) < 8:
        return "Password must be 8+ symbols long."

    # Password must have 1+ number
    if not re.search(r"[0-9]+", password):
        return "Password must have at least 1 number."

    # Password must have 1+ letter
    if not re.search(r"[a-zA-Z]+", password):
        return "Password must have at least 1 letter."

    # Password cannot contain username
    if username in password:
        return "Password cannot contain username."

    return True


def is_possible_user_action(num: str) -> str | Literal[False]:
    """Check if action for user with such number exists"""

    possible_actions = {"1": "view_balance", "2": "deposit", "3": "withdraw", "4": "exit"}
    # Action found
    try:
        action = possible_actions[num]
    # Action not found
    except KeyError:
        action = False
    return action


def is_correct_type(value, type: type) -> bool:
    """Check if value has expected type"""
    return isinstance(value, type)


def can_be_int(value) -> int | Literal[False]:
    """Check if value can be integer"""

    try:
        value = int(value)
    except ValueError:
        value = False
    return value


def is_positive(num: int) -> bool:
    """Check if number is bigger than 0"""
    return num > 0


def is_negative(num: int) -> bool:
    """Check if number is less than 0"""
    return num < 0


def is_enough_in_balance(needed_money: int, username: str) -> bool:
    """Check if user has enough money"""

    balance = get_user(username=username)["balance"]
    return needed_money <= balance


def is_enough_in_atm(needed_money: int) -> bool:
    """Check if atm has enough money"""

    return needed_money <= get_atm_balance()


def has_needed_banknotes(needed_money: int) -> int | Literal[True]:
    """Check if atm has banknotes for needed amount. If not, returns closest smaller available amount"""

    banknotes = get_needed_banknotes(needed_money=needed_money)
    if banknotes["remaining"] == 0:
        return True
    else:
        return needed_money - banknotes["remaining"]


def is_possible_staff_action(num: str) -> str | Literal[False]:
    """Check if action for staff with such number exists"""

    possible_actions = {
        "1": "be_user",
        "2": "view_atm_balance",
        "3": "view_banknotes",
        "4": "change_banknotes",
        "5": "exit",
    }
    # Action found
    try:
        action = possible_actions[num]
    # Action not found
    except KeyError:
        action = False
    return action


def is_existing_denomination(denomination: int) -> bool:
    """Check if available denomination in ATM"""
    banknotes = get_sorted_atm_banknotes()
    denominations = [banknote["denomination"] for banknote in banknotes]
    return denomination in denominations
