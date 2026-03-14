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


def test_():
    """
    docstring.
    """
    pass
