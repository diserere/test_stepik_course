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


def test_():
    """
    docstring.
    """
    pass
