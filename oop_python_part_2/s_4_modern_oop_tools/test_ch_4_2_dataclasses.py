"""4.2 Датаклассы (@dataclass)"""

from dataclasses import dataclass, field
from typing import List

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


def test_frozen_dataclass():
    """
    Задача 3: "Замороженный" датакласс (frozen=True)
    """

    @dataclass(frozen=True)
    class APIConfig:
        base_url: str
        api_key: str

    config = APIConfig("https://example.com", "123456")
    ic(config)

    ic("Try to change base_url")
    try:
        config.base_url = "https://sample.org"  # pyright: ignore[reportAttributeAccessIssue]
        ic(config)
    except Exception as e:
        ic(e)

    ic("Try to change api_key")
    try:
        config.api_key = "abcdef"  # pyright: ignore[reportAttributeAccessIssue]
        ic(config)
    except Exception as e:
        ic(e)


def test_sortable_dataclass():
    """
    Задача 4: Сортируемый датакласс (order=True)
    """

    @dataclass(order=True)
    class Employee:
        salary: int
        name: str

    e = Employee(100, "Mike")
    ic(e)
    ic(e > Employee(100, "John"))
    ic(e > Employee(101, "John"))

    ic("__le__" in vars(Employee))
    ic("__lt__" in vars(Employee))
    ic("__ge__" in vars(Employee))
    ic("__gt__" in vars(Employee))


def test_dataclass_mutable_default_field():
    """
    Задача 5: Датакласс с изменяемым полем по умолчанию
    """

    @dataclass
    class Team:
        name: str
        members: List[str] = field(default_factory=list)

    team = Team("Pythonistas")
    ic(team)
    ic(team.members)
    team.members.append("John")
    ic(team)
    team.members.append(123)  # pyright: ignore[reportArgumentType]
    ic(team)
