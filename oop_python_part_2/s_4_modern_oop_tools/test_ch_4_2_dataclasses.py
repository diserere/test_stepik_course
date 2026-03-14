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


def test_():
    """
    docstring.
    """
    pass
