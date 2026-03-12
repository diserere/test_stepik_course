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


def test_inheritance_order():
    """
    Задача 2: Порядок наследования (MRO)
    """

    class Radio:
        @staticmethod
        def play():
            return "Радио играет"

    class Speaker:
        @staticmethod
        def play():
            return "Колонка играет"

    class Boombox(Radio, Speaker):
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    boombox = Boombox()
    ic(boombox)
    ic(boombox.play())
    ic(boombox.__class__.__mro__)


def test_():
    """
    docstring.
    """
    pass
