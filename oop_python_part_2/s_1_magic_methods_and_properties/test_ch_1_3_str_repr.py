"""1.3 Строковое представление: __str__ и __repr__."""

from icecream import ic


def test_magic_str():
    """
    Задача 1: Реализация __str__
    """

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return f'"{self.title}" автора {self.author}'

    book = Book("1984", "George Orwell")

    ic(book)
    print(book)


def test_magic_repr():
    """
    Задача 2: Реализация __repr__
    """

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"

    point = Point(10, 20)

    ic(point)
    print(point)


def test_repr_as_str_replace():
    """
    Задача 3: __repr__ как замена __str__
    """

    class Player:
        def __init__(self, nickname: str, level: int):
            self.nickname = nickname
            self.level = level

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(nickname={self.nickname!r}, level={self.level!r})"

    player = Player("Gendalf", 100)

    ic(player)
    print(player)


def test_magic_repr_and_str():
    """
    Задача 4: Оба метода в одном классе
    """

    class Order:
        def __init__(self, order_id: int, amount: float):
            self.order_id = order_id
            self.amount = amount

        def __str__(self) -> str:
            return f"Заказ №{self.order_id!r}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(order_id={self.order_id!r}, amount={self.amount!r})"

    order = Order(1, 42)

    ic(order)
    print(order)


def test_str_with_formatting():
    """
    Задача 5: __str__ с форматированием
    """

    class Transaction:
        def __init__(self, amount: float, currency: str):
            self.amount = amount
            self.currency = currency

        def __str__(self) -> str:
            return f"Транзакция на сумму {self.amount:.2f} {self.currency}"

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    t_1 = Transaction(100, "USD")
    ic(t_1)
    print(t_1)

    t_2 = Transaction(0.123, "BTC")
    ic(t_2)
    print(t_2)
