from icecream import ic


def test_char():
    class Character:
        character_count = 0

        def __init__(self, name):
            self.name = name
            Character.character_count += 1

    # ic()
    assert Character.character_count == 0
    ic(Character.character_count)
    char_1 = Character("Bob")  # noqa: F841
    assert Character.character_count == 1
    ic(Character.character_count)
    char_2 = Character("Alice")  # noqa: F841
    assert Character.character_count == 2
    ic(Character.character_count)


def test_method_overload():
    class Device:
        def power_on(self):
            return "Устройство включено"

    class Computer(Device):
        def power_on(self):
            return "Компьютер загружается..."

    ic(Device().power_on())
    ic(Computer().power_on())


def test_method_overload_2():
    class Logger:
        def log(self, message):
            return f"[LOG]: {message}"

    class TimestampLogger(Logger):
        def log(self, message):
            return f"{super().log(message)} (timestamp)"

    ic(Logger().log("test"))
    ic(TimestampLogger().log("test"))


def test_parent_extend():
    class Product:
        def __init__(self, name, price) -> None:
            self.name = name
            self.price = price

    class DiscountedProduct(Product):
        def __init__(self, name, price, discount) -> None:
            super().__init__(name, price)
            self.discount = discount

    product = Product("Product", 100)
    discounted_product = DiscountedProduct("DiscountedProduct", 100, 10)
    for p in (product, discounted_product):
        ic(
            p.name,
            p.price,
            getattr(p, "discount", None),
            # None,
        )


def test_parcial_overload():
    class Vehicle:
        def __init__(self, brand):
            self.brand = brand

        def start_engine(self):
            return "Двигатель запущен"

        def honk(self):
            return "Общий сигнал!"

    class Car(Vehicle):
        def start_engine(self):
            return f"{super().start_engine()}... Проверка систем автомобиля."

        def honk(self):
            return "Би-бип!"

    vehicle = Vehicle("Vehicle")
    ic(vehicle.brand, vehicle.start_engine(), vehicle.honk())

    car = Car("Car")
    ic(car.brand, car.start_engine(), car.honk())


def test_parent_extend_2():
    class Product:
        def __init__(self, name, price) -> None:
            self.name = name
            self.price = price

    class DiscountedProduct(Product):
        def __init__(self, name, price, discount) -> None:
            super().__init__(name, price)
            self.discount = discount

        def get_price_with_discount(self):
            return self.price - (self.price * self.discount / 100)

    product = Product("Product", 100)
    discounted_product = DiscountedProduct("DiscountedProduct", 100, 10)

    ic(
        product.name,
        product.price,
    )
    ic(
        discounted_product.name,
        discounted_product.price,
        discounted_product.discount,
        discounted_product.get_price_with_discount(),
    )
    ic(type(Product))
    ic(type(product))


def test_transport_system():
    # from typing import Literal

    class Vehicle:
        vehicles_created = 0

        def __init__(self, brand, max_speed):
            self.brand = brand
            self._max_speed = max_speed
            self._mileage = 0
            Vehicle.vehicles_created += 1

        def get_max_speed(self):
            return self._max_speed

        def get_mileage(self):
            return self._mileage

        def drive(self, distance):
            self._mileage += distance

        def display_info(self):
            print(f"Марка: {self.brand}")
            print(f"Макс. скорость: {self.get_max_speed()} км/ч")
            print(f"Пробег: {self.get_mileage()} км")

    class Car(Vehicle):
        # def __init__(self, brand, max_speed, engine_type: Literal["Бензин", "Электро"]):
        def __init__(self, brand, max_speed, engine_type):
            super().__init__(brand, max_speed)
            self.engine_type = engine_type

        def display_info(self):
            super().display_info()
            print(f"Тип двигателя: {self.engine_type}")

    class Bicycle(Vehicle):
        def __init__(self, brand, max_speed, frame_material):
            super().__init__(brand, max_speed)
            self.frame_material = frame_material

        def display_info(self):
            super().display_info()
            print(f"Материал рамы: {self.frame_material}")

    # Создаем объекты разных классов
    tesla = Car("Tesla", 250, "Электро")
    bmw = Car("BMW", 280, "Бензин")
    # kamaz = Car("KamAZ", 80, "diezel")
    kamaz = Car("KamAZ", 80, "diezel")  # pyright: ignore[reportArgumentType]
    trek = Bicycle("Trek", 40, "Карбон")

    # Демонстрируем полиморфизм: работаем с разными объектами через общий интерфейс
    # vehicles: list[Vehicle] = [tesla, bmw, trek]
    vehicles: list[Vehicle] = [tesla, bmw, trek, kamaz]
    for vehicle in vehicles:
        print("---")
        vehicle.display_info()  # Один и тот же вызов - разное поведение
        distance = len(vehicle.brand) * 100
        vehicle.drive(distance=distance)
        print(f"Машина проехала {distance} км")
        vehicle.drive(distance=distance)
        print(f"Машина проехала еще {distance} км")
        print(f"Пробег после поездки: {vehicle.get_mileage()} км")

    print("\n" + "=" * 30)
    # Демонстрируем работу атрибута класса
    print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}")


def test_library_system():

    class Publication:
        def __init__(self, title, author, year) -> None:
            self.title = title
            self._author = author
            self._year = year

        def get_info(self):
            return f'"{self.title}" ({self._author}, {self._year})'

    class Book(Publication):
        def __init__(self, title, author, year, isbn) -> None:
            super().__init__(title, author, year)
            self.isbn = isbn

        def get_info(self):
            return super().get_info() + f", ISBN: {self.isbn}"

    class Magazine(Publication):
        def __init__(self, title, editor, year, issue_number) -> None:
            super().__init__(title=title, author=editor, year=year)
            self.issue_number = issue_number
            self._editor = editor

        def get_info(self):
            return f'"{self.title}" (Ред. {self._editor}, {self._year}), Выпуск №{self.issue_number}'

    # Создаем объекты разных классов
    book = Book("Война и мир", "Лев Толстой", 1869, "978-5-389-06254-2")
    magazine = Magazine("National Geographic", "Сьюзан Голдберг", 2021, 8)

    # Демонстрируем полиморфизм
    publications = [book, magazine]
    for pub in publications:
        # Один и тот же вызов - разное поведение
        print(pub.get_info())
