"""2.1 Методы класса (@classmethod)"""

from icecream import ic


def test_simple_classmethod():
    """
    Задача 1: Простой @classmethod
    """

    class GameCharacter:
        def __init__(self, name, level) -> None:
            self.name = name
            self.level = level

        @classmethod
        def create_default_character(cls):
            return cls("Guest", 1)

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    char_custom = GameCharacter("Frodo", 10)
    ic(char_custom)
    char_default = GameCharacter.create_default_character()
    ic(char_default)


def test_create_from_string():
    """
    Задача 2: Создание из строки (from_string)
    """

    class User:
        def __init__(self, username: str, email: str) -> None:
            self.username = username
            self.email = email
            pass

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @classmethod
        def from_string(cls, user_data_string: str):
            username, email = user_data_string.split(",")
            return cls(username, email)

    ic('Try: user_frodo = User("Frodo", "frodo@sheer.com")')
    user_frodo = User("Frodo", "frodo@sheer.com")
    ic(user_frodo)
    ic('Try: user_sam = User.from_string("Sam,sam@sheer.com")')
    user_sam = User.from_string("Sam,sam@sheer.com")
    ic(user_sam)
    ic('Try: user_gollum = User.from_string("Gollum from bad places")')
    try:
        user_gollum = User.from_string("Gollum from bad places")
        ic(user_gollum)
    except Exception as e:
        ic(e)


def test_create_from_dict():
    """
    Задача 3: Создание из словаря (from_dict)
    """

    class Product:
        def __init__(self, name: str, price: float) -> None:
            self.name = name
            self.price = price
            pass

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @classmethod
        def from_dict(cls, product_dict: dict):
            key_name = "name"
            key_price = "price"
            return cls(product_dict[key_name], product_dict[key_price])

    ic('Try: Product("Milk", 0.36)')
    product_milk = Product("Milk", 0.36)
    ic(product_milk)
    ic('Try: Product.from_dict({"name": "Bread", "price": 0.22})')
    product_bread = Product.from_dict({"name": "Bread", "price": 0.22})
    ic(product_bread)
    ic('Try: Product.from_dict({"name": "Oil", "quantity": 1})')
    try:
        product_oil = Product.from_dict({"name": "Oil", "quantity": 1})
        ic(product_oil)
    except Exception as e:
        ic(e)
    ic('Try: Product.from_dict({"name": "Egg", "price": 2.40, "cat": 1})')
    try:
        product_egg = Product.from_dict({"name": "Egg", "price": 2.40, "cat": 1})
        ic(product_egg)
    except Exception as e:
        ic(e)


def test_get_class_attributes():
    """
    Задача 4: @classmethod и атрибуты класса
    """

    class Car:
        total_cars = 0

        def __init__(self, brand: str, model: str) -> None:
            self.brand = brand
            self.model = model
            self.__class__.total_cars += 1

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @classmethod
        def get_total_cars(cls):
            return cls.total_cars

    ic(Car.get_total_cars())
    car_1 = Car("Audi", "X5")
    ic(car_1)
    ic(Car.get_total_cars())
    ic(car_1.get_total_cars())
    car_2 = Car("Kia", "Rio")
    ic(car_2)
    ic(Car.get_total_cars())
    ic(car_2.get_total_cars())


def test_classmethods_inheritance():
    """
    Задача 5: @classmethod в иерархии
    """

    class Website:
        def __init__(self) -> None:
            pass

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @classmethod
        def get_description(cls):
            return "Это общий сайт."

    class Shop(Website):
        @classmethod
        def get_description(cls):
            return "Это интернет-магазин."

    ic(Website.get_description())
    ic(Website().get_description())
    ic(Shop.get_description())
    ic(Shop().get_description())
