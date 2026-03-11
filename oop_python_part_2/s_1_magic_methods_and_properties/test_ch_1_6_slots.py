"""1.6 __slots__: Оптимизация памяти и производительности"""

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
        __slots__ = ("username",)

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


def test_slots_inheritance():
    """
    1.6 __slots__: Оптимизация памяти и производительности

    Задача 3: Наследование и __slots__

    Условие:
    - Эта задача демонстрирует важную особенность поведения __slots__ при наследовании. Если родительский класс использует __slots__ (и не имеет __dict__), а дочерний класс не определяет свой собственный __slots__, то экземпляры дочернего класса снова получат стандартный __dict__.

    Вам нужно:
        1. Создать родительский класс Base.
        2. В классе Base определить __slots__ = ('x',) и __init__(self, x), который устанавливает self.x.
        3. Создать дочерний класс Child, который наследует от Base (class Child(Base):).
        4. Тело класса Child должно быть пустым, используйте оператор pass. В нем не нужно определять __slots__.

    Шаблон кода проверит, что у объекта Base нет __dict__, а у объекта Child он, наоборот, появился.
    """

    class Base:
        __slots__ = ("x",)

        def __init__(self, x: int) -> None:
            self.x = x

    class Child(Base):
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    child = Child(1)
    ic(child)
    ic(hasattr(child, "__dict__"))
    ic(child.__dict__)
    ic(hasattr(child, "__slots__"))
    ic(child.__slots__)

    ic("Add attr y to child")
    try:
        child.y = -1  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(hasattr(child, "y"))
        ic(child)
        ic(child.x)
        ic(child.__slots__)
        ic(child.y)  # pyright: ignore[reportAttributeAccessIssue]
        ic(child.__dict__)


def test_extend_slots_on_inheritance():
    """
    1.6 __slots__: Оптимизация памяти и производительности

    Задача 4: Расширение __slots__ при наследовании

    Условие:
    - Чтобы сохранить оптимизацию по памяти в дочернем классе, он должен сам определить __slots__. При этом в дочернем __slots__ нужно указывать только новые, добавляемые атрибуты, а не повторять родительские.

    Вам нужно:
    1. Создать родительский класс GameObject с __slots__ = ('x', 'y') и __init__(self, x, y).
    2. Создать дочерний класс Player, который наследует от GameObject.
    3. В классе Player определить свой __slots__, указав в нем только один новый атрибут, который вы хотите добавить: ('nickname',).
    4. В Player.__init__ принимать x, y и nickname. Внутри конструктора нужно:
        - Вызвать родительский конструктор с помощью super().__init__(x, y), чтобы установить x и y.
        - Установить новый атрибут self.nickname = nickname.

    Шаблон кода проверит, что у объекта Player есть все три атрибута (x, y, nickname), но при этом у него нет __dict__.
    """

    class GameObject:
        __slots__ = ("x", "y")

        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    class Player(GameObject):
        __slots__ = ("nickname",)

        def __init__(self, x: int, y: int, nickname: str):
            super().__init__(x, y)
            self.nickname = nickname

    player = Player(1, -1, "Frodo")
    ic(hasattr(player, "__dict__"))
    ic(hasattr(player, "__slots__"))
    ic(player.__slots__)
    ic(player.x)
    ic(player.y)
    ic(player.nickname)


def test_slots_and_dict():
    """
    1.6 __slots__: Оптимизация памяти и производительности

    Задача 5: __slots__ и __dict__ вместе

    Условие:
    - Иногда требуется компромисс: оптимизировать хранение известных атрибутов через __slots__, но сохранить возможность добавлять новые, динамические атрибуты. Этого можно достичь, добавив строку '__dict__' в сам __slots__.

    Вам нужно:
    1. Создать класс FlexibleObject.
    2. На уровне класса определить __slots__, который содержит два элемента:
        - Строку с именем основного, "слотового" атрибута: 'fixed_attribute'.
        - Специальную строку '__dict__', которая разрешает создание словаря __dict__ для хранения всех остальных атрибутов.
    3. В __init__ принимать value и устанавливать self.fixed_attribute = value.

    Шаблон кода проверит, что у объекта есть и fixed_attribute, и __dict__, и что в этот __dict__ можно добавлять новые атрибуты.
    """

    class FlexibleObject:
        __slots__ = ("fixed_attribute", "__dict__")

        def __init__(self, value: str) -> None:
            self.fixed_attribute = value

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    f = FlexibleObject("value")
    ic(f)
    ic(f.fixed_attribute)
    ic(f.__slots__)
    ic(f.__dict__)

    ic("Add new_attribute")
    f.new_attribute = "new"  # pyright: ignore[reportAttributeAccessIssue]
    ic(f)
    ic(f.new_attribute)  # pyright: ignore[reportAttributeAccessIssue]
    ic(f.__slots__)
    ic(f.__dict__)
