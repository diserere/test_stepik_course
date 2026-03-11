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


def test_():
    """
    docstring.
    """
    pass
