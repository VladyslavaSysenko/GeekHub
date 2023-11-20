from typing import Literal
from validations import can_be_int, is_possible_staff_action


def get_staff_action() -> str | Literal[False]:
    """Get desired action from staff"""

    # Get user action
    num = input(
        "Available actions:\n\t"
        "1. Continue as user\n\t"
        "2. See ATM balance\n\t"
        "3. See amount of banknotes based on denominations\n\t"
        "4. Change amount of banknotes based on denominations\n\t"
        "5. Exit\n"
        "Enter number of the desired action:"
    )
    # Add new line for nice visual
    print("")
    # Return action or False
    return is_possible_staff_action(num)


def get_changed_denomination() -> tuple[int | Literal[False], int | Literal[False]]:
    """Get denomination and new amount from staff"""

    denomination = input("Enter denomination:")
    amount = input("Enter new amount of banknotes:")
    # Add new line for nice visual
    print("")
    # Check if input can be integer
    return can_be_int(value=denomination), can_be_int(value=amount)
