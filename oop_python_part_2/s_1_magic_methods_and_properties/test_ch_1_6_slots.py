"""1.6 __slots__: Оптимизация памяти и производительности"""

from icecream import ic


def test_slots():
    """
    Задача 1: Простейшее использование __slots__
    """

    class Point:
        __slots__ = ("x", "y")

        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"

    p = Point(1, -1)
    ic(p)
    ic(hasattr(p, "__dict__"))

    try:
        p.i = 2  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(hasattr(p, "i"))


def test_fixed_attributes_list():
    """
    Задача 2: Фиксированный набор атрибутов
    """

    class User:
        __slots__ = ("username",)

        def __init__(self, username) -> None:
            self.username = username

        def __repr__(self):
            return f"{self.__class__.__name__}(username={self.username!r})"

    user = User("John")
    ic(user)
    ic(hasattr(user, "__dict__"))

    try:
        user.email = "john@ya.ru"  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(hasattr(user, "email"))


def test_slots_inheritance():
    """
    Задача 3: Наследование и __slots__
    """

    class Base:
        __slots__ = ("x",)

        def __init__(self, x: int) -> None:
            self.x = x

    class Child(Base):
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    child = Child(1)
    ic(child)
    ic(hasattr(child, "__dict__"))
    ic(child.__dict__)
    ic(hasattr(child, "__slots__"))
    ic(child.__slots__)

    ic("Add attr y to child")
    try:
        child.y = -1  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(hasattr(child, "y"))
        ic(child)
        ic(child.x)
        ic(child.__slots__)
        ic(child.y)  # pyright: ignore[reportAttributeAccessIssue]
        ic(child.__dict__)


def test_extend_slots_on_inheritance():
    """
    Задача 4: Расширение __slots__ при наследовании
    """

    class GameObject:
        __slots__ = ("x", "y")

        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    class Player(GameObject):
        __slots__ = ("nickname",)

        def __init__(self, x: int, y: int, nickname: str):
            super().__init__(x, y)
            self.nickname = nickname

    player = Player(1, -1, "Frodo")
    ic(hasattr(player, "__dict__"))
    ic(hasattr(player, "__slots__"))
    ic(player.__slots__)
    ic(player.x)
    ic(player.y)
    ic(player.nickname)


def test_slots_and_dict():
    """
    Задача 5: __slots__ и __dict__ вместе
    """

    class FlexibleObject:
        __slots__ = ("fixed_attribute", "__dict__")

        def __init__(self, value: str) -> None:
            self.fixed_attribute = value

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    f = FlexibleObject("value")
    ic(f)
    ic(f.fixed_attribute)
    ic(f.__slots__)
    ic(f.__dict__)

    ic("Add new_attribute")
    f.new_attribute = "new"  # pyright: ignore[reportAttributeAccessIssue]
    ic(f)
    ic(f.new_attribute)  # pyright: ignore[reportAttributeAccessIssue]
    ic(f.__slots__)
    ic(f.__dict__)
