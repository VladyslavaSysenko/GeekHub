# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати
# математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути
# пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО
# методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...
# - Додати документування в клас (можете почитати цю статтю:
# https://realpython.com/documenting-python-code/ )

from functools import wraps


def is_float(*args) -> bool:
    return all(isinstance(value, (float, int)) for value in args)


def correct_type(method):
    @wraps(method)
    def wrapper(self, *args):
        # before the method call check input type
        message = is_float(*args)
        if message is not True:
            self.last_result = self._new_result
            self._new_result = "Numbers must be integers or floats."
        else:
            # the actual method call
            method(self, *args)

    return wrapper


class Calc:
    """
    A class for calculations

    Attributes
    ----------
    last_result : str | None | float
        result to the previous math operation. Str type if error (default None)
    _new_result : str | None | float
        result to the new math operation. Str type if error (default None)

    Methods
    -------
    addition(x:float, y:float)
        Makes last_result _new_result and _new_result addition of x and y
    subtraction(x:float, y:float)
        Makes last_result _new_result and _new_result subtraction of x and y
    multiplication(x:float, y:float)
        Makes last_result _new_result and _new_result multiplication of x and y
    division(x:float, y:float)
        Makes last_result _new_result and _new_result division of x on y
    """

    def __init__(self) -> None:
        """
        Parameters
        ----------
        last_result : str | None | float, optional
            result to the previous math operation. Str type if error (default None)
        _new_result : str | None | float, optional
            result to the new math operation. Str type if error (default None)
        """
        self.last_result = None
        self._new_result = None

    @correct_type
    def addition(self, x: float, y: float) -> None:
        """Makes last_result _new_result and _new_result addition of x and y

        _new_result will be "Numbers must be integers or floats." in case of wrong type of parameters.

        Parameters
        ----------
        x : float
            First number got operation
        y : float
            Second number got operation
        """
        self.last_result = self._new_result
        self._new_result = x + y

    @correct_type
    def subtraction(self, x: float, y: float) -> None:
        """Makes last_result _new_result and _new_result subtraction of x and y

        _new_result will be "Numbers must be integers or floats." in case of wrong type of parameters.

        Parameters
        ----------
        x : float
            First number got operation
        y : float
            Second number got operation
        """
        self.last_result = self._new_result
        self._new_result = x - y

    @correct_type
    def multiplication(self, x: float, y: float) -> None:
        """Makes last_result _new_result and _new_result multiplication of x and y

        _new_result will be "Numbers must be integers or floats." in case of wrong type of parameters.

        Parameters
        ----------
        x : float
            First number got operation
        y : float
            Second number got operation
        """
        self.last_result = self._new_result
        self._new_result = x * y

    @correct_type
    def division(self, x: float, y: float) -> None:
        """Makes last_result _new_result and _new_result division of x and y

        _new_result will be "Numbers must be integers or floats." in case of wrong type of parameters.
        _new_result will be "Cannot divide by zero." in case of division by zero.

        Parameters
        ----------
        x : float
            First number got operation
        y : float
            Second number got operation
        """
        self.last_result = self._new_result
        try:
            self._new_result = x / y
        except ZeroDivisionError:
            self._new_result = "Cannot divide by zero."


calc = Calc()
print(calc.last_result)
calc.addition(1, 2.5)
print(calc.last_result)
calc.subtraction(1, 2)
print(calc.last_result)
calc.multiplication(5, 5)
print(calc.last_result)
calc.addition("k", 0)
print(calc.last_result)
calc.division(1, 0)
print(calc.last_result)
calc.subtraction(1, 2)
print(calc.last_result)
