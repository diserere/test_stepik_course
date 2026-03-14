"""4.2 Датаклассы (@dataclass)"""

from dataclasses import dataclass

from icecream import ic


def test_simple_dataclass():
    """
    Задача 1: Простой датакласс
    """

    @dataclass
    class Point:
        x: int
        y: int

    p = Point(1, 2)
    print(p)
    ic(p)

    ic(Point(1, 2))
    ic(p == Point(1, 2))

    ic(p == Point(3, 2))
    ic(p == Point(1, 1))


def test_dataclass_default_values():
    """
    Задача 2: Датакласс со значениями по умолчанию

    """

    @dataclass
    class User:
        username: str
        is_active: bool = True
        level: int = 1

    u = User("Mike")
    ic(u)
    u.level += 1
    u.is_active = False
    ic(u)

    ic(u == User("Mike"))
    ic(u == User("Mike", False, 2))


def test_():
    """
    docstring.
    """
    pass
