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


def test_str_with_formatting():
    """
    1.3 Строковое представление: __str__ и __repr__.

    Задача 5: __str__ с форматированием

    Условие:
    1. Создайте класс с именем Transaction.
    2. Реализуйте конструктор __init__:
        - Он должен принимать два аргумента при создании объекта:
            - amount (сумма) — числовое значение (целое или с плавающей точкой).
            - currency (валюта) — строка (например, "RUB", "USD").
        - Эти значения должны сохраняться как атрибуты объекта.
    3. Реализуйте специальный метод __str__:
        - Этот метод должен возвращать строку, описывающую транзакцию.
        - Формат строки должен быть строго следующим: "Транзакция на сумму <сумма> <валюта>".
        - Важное условие форматирования: Сумма (amount) всегда должна отображаться с двумя знаками после запятой, даже если изначально она была целым числом.
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


def test_add_vectors():
    """
    1.4 Перегрузка операторов

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
    1.4 Перегрузка операторов

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
    1.4 Перегрузка операторов

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
    1.4 Перегрузка операторов

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
    1.4 Перегрузка операторов

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


def test_property():
    """
    1.5 Свойства (@property): элегантная инкапсуляция

    Задача 1: Простой @property (Только для чтения)

    Условие:
    - Ваша задача — превратить метод-геттер в атрибут "только для чтения" с помощью декоратора @property.
    - Вам нужно:
        1. Создать класс Circle (Круг).
        2. В __init__ он должен принимать radius (радиус) и сохранять его в защищенный атрибут self._radius.
        3. Создать метод area() (площадь), который вычисляет и возвращает площадь круга по формуле π * r². Для π используйте значение 3.14159.
        4. Превратить метод area в свойство, применив к нему декоратор @property. Это позволит обращаться к нему как к атрибуту (my_circle.area), а не вызывать как метод (my_circle.area()).
    """

    class Circle:
        PI = 3.14159

        def __init__(self, radius) -> None:
            self._radius = radius

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @property
        def area(self):
            return self.PI * self._radius**2

    circle = Circle(10)
    ic(circle)

    ic(circle.area)
