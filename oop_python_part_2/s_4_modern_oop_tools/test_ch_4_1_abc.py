"""4.1 Абстрактные базовые классы (ABC)"""

from abc import ABC, abstractmethod

from icecream import ic


def test_simple_abc():
    """
    Задача 1: Создание простого абстрактного класса
    """

    class Shape(ABC):
        @abstractmethod
        def area(self): ...

    try:
        abc_obj = Shape()  # pyright: ignore[reportAbstractUsage]
        ic(abc_obj)
    except Exception as e:
        ic(e)


def test_implement_abc():
    """
    Задача 2: Реализация абстрактного класса
    """

    class Shape(ABC):
        @abstractmethod
        def area(self): ...

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in self.__dict__.items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    class Square(Shape):
        def __init__(self, side: int) -> None:
            super().__init__()
            self.side = side

        def area(self):
            return self.side**2

    try:
        sqare = Square(2)
        ic(sqare)
        ic(sqare.area())
    except Exception as e:
        ic(e)


def test_abc_with_several_methods():
    """
    Задача 3: Контракт из нескольких методов
    """

    class DataSource(ABC):
        @abstractmethod
        def read(): ...
        @abstractmethod
        def write(data): ...

    class FileStorage(DataSource):
        def __init__(self) -> None:
            super().__init__()

        @staticmethod
        def read():
            return "Чтение из файла"

        @staticmethod
        def write(data):
            return f"Запись в файл: {data}"

    fs = FileStorage
    ic(fs.read())
    ic(fs.write("qwerty"))
    ic(fs.write(3.14))


def test_abc_with_concrete_methods():
    """
    Задача 4: Абстрактный класс с конкретными методами
    """

    class Instrument(ABC):
        def __init__(self, brand) -> None:
            self.brand = brand

        def show_brand(self):
            return f"Бренд: {self.brand}"

        @abstractmethod
        def play(): ...

    class Guitar(Instrument):
        @staticmethod
        def play():
            return "Играет мелодия на гитаре"

    guitar = Guitar("Gibson")
    ic(guitar.show_brand())
    ic(guitar.play())


def test_polymorphic_argument():
    """
    Задача 5: Практический пример "Плагины"
    """

    class Plugin(ABC):
        @abstractmethod
        def execute(self, data: str): ...

    class UpperCasePlugin(Plugin):
        @staticmethod
        def execute(data: str):
            return data.upper()

    class LowerCasePlugin(Plugin):
        @staticmethod
        def execute(data: str):
            return data.lower()

    def run_plugins(plugins: list[Plugin], data: str):
        return [p.execute(data) for p in plugins]

    ic(run_plugins([UpperCasePlugin(), LowerCasePlugin()], "Some 3 Words"))
