"""4.1 Абстрактные базовые классы (ABC)"""

from abc import ABC, abstractmethod

from icecream import ic


def test_simple_abc():
    """
    Задача 1: Создание простого абстрактного класса
    Условие:
    Ваша задача — создать "интерфейс" или "контракт" для всех геометрических фигур, которые могут иметь площадь.

    Вам нужно:

    Импортировать ABC и abstractmethod из модуля abc.

    Создать абстрактный базовый класс Shape, который наследует от ABC.

    Внутри Shape определить абстрактный метод area(self). Тело метода может быть пустым (pass).

    Шаблон кода проверит, что вы правильно создали класс и что от него нельзя создать экземпляр.

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


def test_():
    """
    docstring.
    """
    pass
