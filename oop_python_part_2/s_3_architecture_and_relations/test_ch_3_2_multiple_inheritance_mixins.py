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
            variables = [f"{k}={v!r}" for k, v in self.__dict__.items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    boombox = Boombox()
    ic(boombox)
    ic(boombox.play())
    ic(boombox.__class__.__mro__)


def test_rombic_inheritance():
    """
    Задача 3: "Проблема ромба" и super()
    """

    class Base:
        @staticmethod
        def get_info():
            return "Base"

    class Left(Base):
        def get_info(self):
            return super().get_info() + "-Left"

    class Right(Base):
        def get_info(self):
            return super().get_info() + "-Right"

    class Child(Left, Right):
        def get_info(self):
            return super().get_info() + "-Child"

    ic(Base().get_info())
    ic(Base.__mro__)
    ic(Left().get_info())
    ic(Left.__mro__)
    ic(Right().get_info())
    ic(Right.__mro__)
    ic(Child().get_info())
    ic(Child.__mro__)


def test_simple_mixin():
    """
    Задача 4: Простой Миксин (ReprMixin)
    """

    class ReprMixin:
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith("_")]
            return f"{type(self).__name__}({', '.join(variables)})"

    class SomeClass:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
            self._private_attr = "Private"
            self.__protected_attr = "Secret"

    class PrettyClass(SomeClass, ReprMixin): ...

    ic('pretty_obj = PrettyClass("Pretty", 13)')
    pretty_obj = PrettyClass("Pretty", 13)
    ic(pretty_obj.__dict__)
    ic(pretty_obj)


def test_practical_mixin():
    """
    Задача 5: Практический Миксин (DictMixin)
    """

    class DictMixin:
        def to_dict(self):
            return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    class ReprMixin:
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith("_")]
            return f"{type(self).__name__}({', '.join(variables)})"

    class User:
        def __init__(self, name: str, email: str):
            self.name = name
            self.email = email
            self._password_hash: str | None = None

    class SerializableUser(User, ReprMixin, DictMixin): ...

    user = SerializableUser("Frodo", "frodo@sheer.uk")
    ic(user)
    ic(user.to_dict())

    user_2 = SerializableUser(**user.to_dict())
    ic(user_2)
    ic(user_2.to_dict())
