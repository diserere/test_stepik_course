"""2.2 Статические методы (@staticmethod)"""

from icecream import ic


def test_staticmethod_format_email():
    """
    Задача 1: Простая утилита
    """

    class Formatter:
        @staticmethod
        def format_email(email: str):
            if isinstance(email, str) and "@" in email:
                return email.lower().strip()

    ic(Formatter.format_email("   My_EMAil@dot.coM"))
    ic(Formatter.format_email("   My_EMAil@DOT.coM   "))
    ic(Formatter.format_email("   My_EMAil @ DOT.coM   "))
    ic(Formatter.format_email("   \nMy_EMAil@dot.coM"))
    ic(Formatter.format_email("   \nMy_EMAil DOT.coM   "))
    ic(Formatter.format_email(["my_email@dot.com"]))  # pyright: ignore[reportArgumentType]
    ic(Formatter.format_email(123))  # pyright: ignore[reportArgumentType]


def test_staticmethod_library():
    """
    Задача 2: Класс-библиотека
    """

    class Validator:
        @staticmethod
        def is_positive(number: int | float):
            return isinstance(number, (int, float)) and number > 0

        @staticmethod
        def is_even(number: int):
            return isinstance(number, (int)) and number % 2 == 0

    ic(Validator.is_positive(-1))
    ic(Validator.is_positive(-10.5))
    ic(Validator.is_positive(0))
    ic(Validator.is_positive(0.1))
    ic(Validator.is_positive(1))
    ic(Validator.is_positive("1"))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(-2))
    ic(Validator.is_even(-1))
    ic(Validator.is_even(-0.2))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(-0.1))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(0))
    ic(Validator.is_even(0.1))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(0.2))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(1))
    ic(Validator.is_even(2))
    ic(Validator.is_even("1"))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even("2"))  # pyright: ignore[reportArgumentType]


def test_():
    """
    docstring.
    """
    pass
