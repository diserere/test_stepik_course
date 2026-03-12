"""3.2 Множественное наследование и Миксины"""

from icecream import ic


def test_multiple_inheritance():
    """
    Задача 1: Простое множественное наследование
    """

    class Swimmer:
        @staticmethod
        def swim():
            return "Я плыву"

    class Walker:
        @staticmethod
        def walk():
            return "Я иду"

    class Amphibian(Swimmer, Walker): ...

    frog = Amphibian()
    ic(frog.swim())
    ic(frog.walk())


def test_():
    """
    docstring.
    """
    pass
