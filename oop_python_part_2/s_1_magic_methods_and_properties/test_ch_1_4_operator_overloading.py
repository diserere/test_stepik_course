"""1.4 Перегрузка операторов"""

from icecream import ic


def test_add_vectors():
    """
    Задача 1: Сложение векторов (__add__)
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

