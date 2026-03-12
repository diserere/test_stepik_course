"""1.5 Свойства (@property): элегантная инкапсуляция"""
from icecream import ic


def test_property():
    """
    Задача 1: Простой @property (Только для чтения)
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

    ic("Create converter:")
    c = Converter()
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    ic("Test set meters: 12.34")
    c.meters = 12.34
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    ic("Test set meters: str('111')")
    c.meters = "111"
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    ic("Test set kilometers: 56.789")
    c.kilometers = 56.789
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    ic("Test set kilometers: str('222')")
    c.kilometers = "222"
    ic(c)
    ic(c.meters)
    ic(c.kilometers)

    ic("Reset meters to 100")
    c.meters = 100
    ic(c)

    ic("Test set meters (negative): str('asd333')")
    c.meters = "asd333"
    ic(c)

    ic("Test set kilometers (negative): str('444cde')")
    c.kilometers = "444cde"
    ic(c)
