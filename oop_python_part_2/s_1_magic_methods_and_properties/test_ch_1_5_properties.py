"""1.5 Свойства (@property): элегантная инкапсуляция"""
from icecream import ic


def test_property():
    """
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
