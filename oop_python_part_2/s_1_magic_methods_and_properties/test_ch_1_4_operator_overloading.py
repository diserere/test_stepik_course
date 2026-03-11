"""1.4 Перегрузка операторов"""

from icecream import ic


def test_add_vectors():
    """
    Задача 1: Сложение векторов (__add__)

    Условие:
    - Ваша задача — научить объекты класса Vector складываться друг с другом с помощью оператора +.
    - Вам нужно:
        1. Создать класс Vector.
        2. В методе __init__ он должен принимать два аргумента, x и y, и сохранять их в одноименные атрибуты self.x и self.y.
        3. Реализовать метод __add__(self, other). Этот метод будет вызываться при сложении двух векторов (v1 + v2). Он должен:
            - Принимать другой объект Vector в качестве аргумента other.
            - Возвращать (return) новый объект Vector.
            - Координаты нового вектора должны быть равны сумме координат исходных векторов (т.е. self.x + other.x и self.y + other.y).
        4. Реализовать метод __repr__(self). Для корректной работы тестов и наглядного вывода он должен возвращать строку в строго заданном формате, например, для вектора с x=1 и y=2 строка должна быть Vector(1, 2).
    """

    class Vector:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{type(self).__name__}({self.x}, {self.y})"

        def __add__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return self.__class__(self.x + other.x, self.y + other.y)

    vector_1 = Vector(1, 1)
    vector_2 = Vector(2, -2)

    sum_vector = vector_1 + vector_2
    ic(sum_vector)
    print(sum_vector)

    try:
        fake_vector = vector_1 + 10
    except Exception as e:
        ic(e)
    finally:
        try:
            ic(fake_vector)
        except Exception as e:
            ic(e)


def test_eq_objects():
    """
    Задача 2: Сравнение объектов (__eq__)

    Условие:
    - По умолчанию объекты сравниваются по их адресу в памяти. Ваша задача — научить объекты класса Person правильно сравниваться на равенство (==) по их содержимому.
    - Вам нужно:
        1. Создать класс Person.
        2. В методе __init__ он должен принимать два аргумента, name и age, и сохранять их в одноименные атрибуты.
        3. Реализовать метод __eq__(self, other). Этот метод будет вызываться при сравнении (p1 == p2). Он должен:
            - Принимать другой объект в качестве аргумента other.
            - Возвращать True, если у self и other совпадают и name, и age.
            - Возвращать False во всех остальных случаях (если other не является объектом Person или если атрибуты не совпадают).
            - Подсказка: Перед сравнением атрибутов убедитесь, что other является экземпляром класса Person с помощью isinstance().
    """

    class Person:
        def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

        def __eq__(self, other) -> bool:
            if not isinstance(other, self.__class__):
                return NotImplemented
            return self.age == other.age and self.name == other.name

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    person_1 = Person("Alice", 21)
    person_2 = Person("Alice", 21)
    person_3 = Person("Bob", 21)
    person_4 = Person("Alice", 22)

    ic(
        person_1,
        person_2,
        person_3,
        person_4,
    )

    ic(person_1 == person_2)
    ic(person_1 == person_3)
    ic(person_1 == person_4)

    try:
        is_equal_to_str = person_1 == "Alice"
    except Exception as e:
        ic(e)
    finally:
        try:
            ic(is_equal_to_str)
        except Exception as e:
            ic(e)


def test_magic_len():
    """
    Задача 3: Получение длины (__len__)

    Условие:
    - Научите ваш кастомный объект сообщать свою "длину" через встроенную функцию len().
    - Вам нужно:
        1. Создать класс Playlist.
        2. В методе __init__ он должен принимать два аргумента: title (название плейлиста) и songs (список строк с названиями песен). Сохраните их в одноименные атрибуты.
        3. Реализовать метод __len__(self). Этот метод будет вызываться при len(playlist). Он должен:
            - Возвращать (return) целое число, равное количеству песен в плейлисте (т.е. длине списка self.songs).
    """

    class Playlist:
        def __init__(self, title: str, songs: list[str]) -> None:
            self.title = title
            self.songs = songs

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def __len__(self) -> int:
            return len(self.songs)

    playlist = Playlist("My Playlist", ["Song 1", "Song 2", "Song 3"])
    ic(playlist, len(playlist))


def test_magic_getitem():
    """
    Задача 4: Доступ по индексу (__getitem__)

    Условие:
    - Научите ваш объект вести себя как словарь, позволяя получать доступ к его внутренним данным через синтаксис квадратных скобок ([]).
    - Вам нужно:
        1. Создать класс Grades (Оценки).
        2. В методе __init__ не нужно принимать никаких аргументов. Вместо этого создайте внутри него защищенный атрибут self._grades и присвойте ему словарь с оценками: {"math": 5, "history": 4}.
        3. Реализовать метод __getitem__(self, subject). Этот метод будет вызываться при обращении grades["math"]. Он должен:
            - Принимать subject (название предмета в виде строки).
            - Возвращать (return) оценку для этого предмета из внутреннего словаря self._grades.
    """

    class Grades:
        def __init__(self) -> None:
            self._grades = {"math": 5, "history": 4}

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def __getitem__(self, subject):
            # return self._grades.get(subject, 0)
            return self._grades[subject]

    grades = Grades()
    ic(grades)

    ic(grades["math"])
    ic(grades["history"])
    try:
        ic(grades["science"])
    except Exception as e:
        ic(e)


def test_magic_lt():
    """
    Задача 5: Сортировка объектов (__lt__)

    Условие:
    - Научите объекты класса Item (Предмет) быть сортируемыми. Встроенная функция sorted() сможет работать с вашими объектами, если вы объясните ей, какой из двух объектов считать "меньше".
    - Вам нужно:
        1. Создать класс Item.
        2. В методе __init__ он должен принимать name и price.
        3. Реализовать метод __lt__(self, other). lt означает "less than" (меньше чем). Метод будет вызываться при сравнении item1 < item2. Он должен:
            - Принимать другой объект Item в качестве other.
            - Возвращать True, если цена self.price строго меньше цены other.price.
            - Возвращать False во всех остальных случаях.
        4. Реализовать метод __repr__(self). Для корректной работы тестов и наглядного вывода он должен возвращать строку в формате Item('[name]', [price]), например: Item('Телефон', 50000).
    """

    class Item:
        def __init__(self, name: str, price: float) -> None:
            self.name = name
            self.price = price

        def __repr__(self):
            return f"{type(self).__name__}({self.name!r}, {self.price!r})"

        def __lt__(self, other):
            if not isinstance(other, self.__class__):
                return NotImplemented
            return self.price < other.price

    item_1 = Item("Item 1", 2)
    item_2 = Item("Item 2", 2)
    item_3 = Item("Item 3", 3)
    item_4 = Item("Item 4", 1)

    ic(item_1)
    ic(item_2)
    ic(item_3)
    ic(item_4)

    ic(item_1 < item_2)
    ic(item_1 < item_3)
    ic(item_1 < item_4)
    try:
        ic(item_1 < 3)
    except Exception as e:
        ic(e)

