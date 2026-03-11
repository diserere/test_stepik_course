from icecream import ic


def test_slots():
    """
    1.6 __slots__: Оптимизация памяти и производительности

    Задача 1: Простейшее использование __slots__

    Условие:
    - Ваша задача — создать простой класс Point, оптимизированный по памяти. По умолчанию Python хранит атрибуты в словаре __dict__, что затратно. Использование __slots__ отключает этот механизм, экономя память.

    Вам нужно:
    1. Создать класс с именем Point.
    2. На уровне класса (сразу после строки class Point:) определить специальный атрибут __slots__.
    3. Присвоить __slots__ кортеж строк, содержащий имена всех атрибутов, которые будут у экземпляров этого класса. В нашем случае это ('x', 'y').
    4. Создать метод __init__(self, x, y), который принимает x и y и присваивает их соответствующим атрибутам self.x и self.y.

    Шаблон кода проверит, что после этих действий у созданного объекта Point действительно отсутствует словарь __dict__.
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
    1.6 __slots__: Оптимизация памяти и производительности

    Задача 2: Фиксированный набор атрибутов

    Условие:
    - Одним из главных следствий использования __slots__ является то, что вы больше не можете добавлять к экземпляру новые атрибуты, которые не были заранее объявлены в __slots__. Это делает структуру объекта более строгой и предсказуемой.

    Вам нужно:
    1. Создать класс User.
    2. На уровне класса определить __slots__ и указать в нем только один разрешенный атрибут — 'username'.
    3. Создать метод __init__(self, username), который устанавливает значение для self.username.

    Шаблон кода попытается создать объект вашего класса, а затем добавить к нему новый атрибут email. Тест будет пройден, если эта попытка вызовет ожидаемую ошибку AttributeError, подтверждая, что __slots__ работает правильно.
    """

    class User:
        __slots__ = ["username"]

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
