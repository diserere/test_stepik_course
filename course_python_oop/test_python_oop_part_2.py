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


def test_property_setter():
    """
    1.5 Свойства (@property): элегантная инкапсуляция

    Задача 2: @property и @*.setter

    Условие:
    - Теперь давайте создадим полноценное свойство, которое можно и читать, и безопасно изменять.
    - Вам нужно:
        1. Создать класс Temperature.
        2. В __init__ создать защищенный атрибут self._celsius со значением 0.
        3. Создать свойство celsius для доступа к self._celsius:
            - Геттер (с @property): должен просто возвращать self._celsius.
            - Сеттер (с @celsius.setter): должен принимать новое значение new_celsius и, если оно не ниже абсолютного нуля (-273.15), присваивать его self._celsius. Если значение некорректно, атрибут меняться не должен.
    """

    class Temperature:
        ABSOLUTE_ZERO = -273.15

        def __init__(self) -> None:
            self._celsius: float = 0

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, new_celsius: float):
            if isinstance(new_celsius, (int, float)) and new_celsius >= self.ABSOLUTE_ZERO:
                self._celsius = new_celsius
            # else:
            #     raise ValueError(
            #         f"Значение должно быть (int, float) и не может быть ниже абсолютного нуля ({self.ABSOLUTE_ZERO})"
            #     )

    t = Temperature()
    ic(t)
    ic(t.celsius)
    t.celsius = 22
    ic(t.celsius)
    t.celsius = -35.6
    ic(t.celsius)
    try:
        t.celsius = -350
    except Exception as e:
        ic(e)
    finally:
        ic(t.celsius)
    try:
        t.celsius = "356"  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(t.celsius)


def test_calculated_property():
    """
    1.5 Свойства (@property): элегантная инкапсуляция

    Задача 3: Вычисляемое свойство

    Условие:
        - Свойства могут не только возвращать сохраненные значения, но и вычислять их "на лету".
        - Вам нужно:
            1. Создать класс Rectangle (Прямоугольник).
            2. В __init__ он должен принимать width (ширина) и height (высота) и сохранять их в одноименные публичные атрибуты.
            3. Создать свойство только для чтения area (площадь), которое:
                - Не хранит значение в отдельном атрибуте.
                - При каждом обращении вычисляет и возвращает произведение self.width * self.height.
    """

    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            self.width = width
            self.height = height

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @property
        def area(self):
            return self.width * self.height

    rectangle = Rectangle(3.5, 4)
    ic(rectangle)
    ic(rectangle.area)

    rectangle.width = 5
    ic(rectangle)
    ic(rectangle.area)

    try:
        rectangle.area = 100500  # pyright: ignore[reportAttributeAccessIssue]
    except Exception as e:
        ic(e)
    finally:
        ic(rectangle.area)


def test_setter_with_type_conversion():
    """
    1.5 Свойства (@property): элегантная инкапсуляция

    Задача 4: Сеттер с преобразованием типа

    Условие:
    - Сеттер может не только проверять, но и преобразовывать данные перед сохранением.
    - Вам нужно:
        1. Создать класс Config.
        2. В __init__ создать защищенный атрибут self._port со значением 80.
        3. Создать свойство port для доступа к self._port:
            - Геттер должен возвращать self._port.
            - Сеттер должен принимать new_port. Перед сохранением он должен всегда преобразовывать new_port в целое число (int). Если преобразование невозможно (например, передали строку "abc"), он должен игнорировать изменение.
    """

    class Config:
        def __init__(self) -> None:
            self._port: int = 80

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @property
        def port(self):
            return self._port

        @port.setter
        def port(self, new_port):
            try:
                port = int(new_port)
            except Exception:
                pass
            else:
                self._port = port

    config = Config()
    ic(config)
    ic(config.port)

    config.port = 443.5
    ic(config.port)

    try:
        config.port = "22"
    except Exception as e:
        ic(e)
    finally:
        ic(config.port)

    try:
        config.port = "8080abc"
    except Exception as e:
        ic(e)
    finally:
        ic(config.port)


def test_linked_properties():
    """
    1.5 Свойства (@property): элегантная инкапсуляция

    Задача 5: Полный цикл: два связанных свойства

    Описание:
    - Вам нужно реализовать класс Converter, который хранит расстояние. Особенность класса в том, что он позволяет работать с одной и той же дистанцией как в метрах, так и в километрах. Изменение одной величины должно автоматически обновлять другую.

    Технические требования:
    1. Класс Converter:
        - При создании экземпляра класса (в методе __init__) не нужно принимать никаких аргументов.
        - Внутри __init__ создайте защищенный атрибут self._meters и установите его значение равным 0. Это будет наше основное хранилище данных.
    2. Свойство meters:
        - Геттер (@property): Возвращает текущее значение self._meters.
        - Сеттер (@meters.setter): Принимает новое значение и записывает его напрямую в self._meters.
    3. Свойство kilometers:
        - Геттер (@property): Не хранит отдельное значение! Он должен взять текущее значение self._meters, перевести его в километры (разделить на 1000) и вернуть результат.
        - Сеттер (@kilometers.setter): Принимает значение в километрах. Метод должен перевести полученные километры в метры (умножить на 1000) и сохранить результат в общий атрибут self._meters.

    Суть задачи:
    - У вас есть только одна переменная (_meters), но два способа доступа к ней. Свойство kilometers работает как "умная обертка" над метрами.
    """

    class Converter:
        M_PER_KM = 1000

        def __init__(self) -> None:
            self._meters: float = 0

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @property
        def meters(self):
            return self._meters

        @meters.setter
        def meters(self, new_value):
            try:
                value = float(new_value)
            except Exception:
                pass
            else:
                self._meters = value

        @property
        def kilometers(self):
            return self._meters / self.M_PER_KM

        @kilometers.setter
        def kilometers(self, new_value):
            try:
                value = float(new_value)
            except Exception:
                pass
            else:
                self._meters = value * self.M_PER_KM

    print("Create converter")
    c = Converter()
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    print("Test set meters: 12.34")
    c.meters = 12.34
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    print("Test set meters: str('111')")
    c.meters = "111"
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    print("Test set kilometers: 56.789")
    c.kilometers = 56.789
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    print("Test set kilometers: str('222')")
    c.kilometers = "222"
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    print("Reset meters to 100")
    c.meters = 100
    ic(c)

    print("Test set meters (negative): str('asd333')")
    c.meters = "asd333"
    ic(c)

    print("Test set kilometers (negative): str('444cde')")
    c.kilometers = "444cde"
    ic(c)


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
