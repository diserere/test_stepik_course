from icecream import ic


def test_magic_str():
    """
    1.3 Строковое представление: __str__ и __repr__.

    Задача 1: Реализация __str__

    Условие:
        Создайте класс Book.
        1. В __init__ он должен принимать title и author.
        2. Реализуйте метод __str__ так, чтобы он возвращал строку в формате: "[title]" автора [author].
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
    1.3 Строковое представление: __str__ и __repr__.

    Задача 2: Реализация __repr__

    Условие:
        Создайте класс Point (Точка).
        1. В __init__ он должен принимать x и y.
        2. Реализуйте метод __repr__ так, чтобы он возвращал строку, имитирующую вызов конструктора, например: Point(x=10, y=20).
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
    1.3 Строковое представление: __str__ и __repr__.

    Задача 3: __repr__ как замена __str__

    Условие:
        Создайте класс Player.
        1. В __init__ он должен принимать nickname и level.
        2. Реализуйте только метод __repr__, который возвращает строку в формате: Player(nickname='[nickname]', level=[level]).
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
    1.3 Строковое представление: __str__ и __repr__.

    Задача 4: Оба метода в одном классе

    Условие:
        Создайте класс Order (Заказ):
        1. В __init__ он принимает order_id и amount.
        2. Метод __str__ должен возвращать простую строку: "Заказ №[order_id]".
        3. Метод __repr__ должен возвращать техническую строку: "Order(order_id=[order_id], amount=[amount])".
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
