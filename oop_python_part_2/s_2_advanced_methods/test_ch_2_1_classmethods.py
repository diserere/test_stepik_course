"""2.1 Методы класса (@classmethod)"""

from icecream import ic


def test_simple_classmethod():
    """
    Задача 1: Простой @classmethod
    """

    class GameCharacter:
        def __init__(self, name, level) -> None:
            self.name = name
            self.level = level

        @classmethod
        def create_default_character(cls):
            return cls("Guest", 1)

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    char_custom = GameCharacter("Frodo", 10)
    ic(char_custom)
    char_default = GameCharacter.create_default_character()
    ic(char_default)


def test_():
    """
    docstring.
    """
    pass
