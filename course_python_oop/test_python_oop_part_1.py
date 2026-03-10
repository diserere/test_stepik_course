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


def test_game_characters():
    from time import sleep

    class GameObject:
        def __init__(self, name) -> None:
            self.name = name

        def get_status(self):
            return f"-- Имя: {self.name}"

    class Character(GameObject):
        def __init__(self, name, damage) -> None:
            # self.name = name
            super().__init__(name)
            self._health = 100
            self._damage = damage

        # def attack(self, target: "Character"):
        def attack(self, target: GameObject):
            print(f"{self.name} атакует {target.name}")
            # if hasattr(target, "take_damage"):
            if isinstance(target, Character):
                print(f"-- {self.name} атаковал {target.name} с силой {self._damage}")
                target.take_damage(self._damage)
            else:
                print(f"-- {target.name} нельзя нанести урон")
            self.get_status()

        def take_damage(self, amount):
            self._health -= amount
            print(f"-- {self.name} получил урон {amount}")
            self.get_status()

        def get_health(self):
            return self._health

        def get_status(self):
            return super().get_status() + f", Здоровье: {self.get_health()}"

    class Warrior(Character):
        def __init__(self, name, damage, armor) -> None:
            super().__init__(name, damage)
            self._armor = armor

        def get_armor(self):
            return self._armor

        def set_armor(self, armor):
            self._armor = armor
            print(f"Прочность брони у {self.name} изменилось до {self.get_armor()}")

        def take_damage(self, amount):
            amount = max(0, amount - self._armor)
            super().take_damage(amount)

        def get_status(self):
            return super().get_status() + f", Броня: {self.get_armor()}"

    class Mage(Character):
        def __init__(self, name, damage, mana) -> None:
            super().__init__(name, damage)
            self.mana = mana

        def get_mana(self):
            return self.mana

        def set_mana(self, mana):
            self.mana = mana
            print(f"Количество маны у {self.name} изменилось до {self.get_mana()}")

        # def attack(self, target: Character):
        def attack(self, target: GameObject):
            print(f"{self.name} собирает магическую силу для атаки")
            attack_cost = 10
            if self.get_mana() >= attack_cost:
                super().attack(target)
                # self._mana -= attack_cost
                self.set_mana(self.get_mana() - attack_cost)
            else:
                print(
                    f"-- {self.name} не может атаковать {target.name}: недостаточно маны ({self.get_mana()}) "
                    f"для нанесения удара ({attack_cost})"
                )

        def get_status(self):
            return super().get_status() + f", Мана: {self.get_mana()}"

    # Создаем персонажей
    warrior = Warrior("Конан", 15, 5)  # Урон 15, Броня 5
    mage = Mage("Раистлин", 20, 100)  # Урон 20, Мана 100
    stone = GameObject("Камень")

    print(warrior.get_status())
    print(mage.get_status())
    print(stone.get_status())

    print("--- Битва ---")

    # Маг атакует воина
    mage.attack(warrior)
    print("--", warrior.get_status())  # Воин должен получить 15 урона (20 - 5 брони)

    # Воин атакует мага
    warrior.attack(mage)
    print("--", mage.get_status())  # Маг должен получить 15 урона

    # Маг атакует камень
    mage.attack(stone)
    print("--", mage.get_status())  # Маг должен получить -t0 маны
    print("--", stone.get_status())

    # Проверка логики мага
    # mage.mana = 5 # Устанавливаем мало маны
    small_mana = 5
    print("--", f"Меняем магу ману до {small_mana}")
    mage.set_mana(small_mana)  # Устанавливаем мало маны
    mage.attack(warrior)
    print("--", warrior.get_status())  # Здоровье воина не должно измениться

    print()
    print("*" * 20)
    print()
    print("---- Турнир ----")
    print()

    round = 1
    round_pair: list[Character] = [mage, warrior]
    # Восстанавливаем ману магу
    # mage.set_mana(40)
    # mage.set_mana(100)
    # mage.set_mana(111)
    mage.set_mana(123)
    # Меняем защиту воину
    warrior.set_armor(6)
    print()

    while True:
        attacker, target = round_pair
        print(f"---- Раунд {round}: [ {attacker.name} ] vs [ {target.name} ]")

        print()
        # Первый персонаж атакует камень
        attacker.attack(stone)

        print()
        # Первый персонаж атакует второго
        attacker.attack(target)

        print()
        print("- Итоги раунда:")
        print(attacker.get_status())  # Воин должен получить 15 урона (20 - 5 брони)
        print(target.get_status())  # Воин должен получить 15 урона (20 - 5 брони)
        if target.get_health() <= 0:
            print()
            print(f"Турнир окончен: {target.name} погиб.")
            break

        print()
        sleep(1)
        round_pair = round_pair[::-1]
        round += 1
