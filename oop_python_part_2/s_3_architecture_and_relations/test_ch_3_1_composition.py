"""3.1 Композиция вместо наследования"""

from icecream import ic


def test_simple_relation_has_a():
    """
    Задача 1: Простое отношение "has-a"
    """

    class Brain:
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    class Person:
        def __init__(self, name) -> None:
            self.name = name
            self.brain = Brain()

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    person = Person("Pinky")
    ic(person)


def test_call_delegation():
    """
    Задача 2: Делегирование вызова
    """

    class CPU:
        @staticmethod
        def calculate():
            return "Вычисления..."

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    class Computer:
        def __init__(self) -> None:
            self.cpu = CPU()

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def run(self):
            return self.cpu.calculate()

    computer = Computer()
    ic(computer)
    ic(computer.run())


def test_multiple_composition():
    """
    Задача 3: Композиция из нескольких объектов
    """

    class Engine:
        @staticmethod
        def start():
            return "Двигатель запущен"

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    class Wheels:
        @staticmethod
        def rotate():
            return "Колеса вращаются"

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    class Car:
        def __init__(self):
            self.engine = Engine()
            self.wheels = Wheels()

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def drive(self):
            return f"{self.engine.start()} и {self.wheels.rotate()}"

    car = Car()
    ic(car)
    ic(car.engine)
    ic(car.engine.start())
    ic(car.wheels)
    ic(car.wheels.rotate())
    ic(car.drive())


def test_composition_with_objects_list():
    """
    Задача 4: Композиция со списком объектов
    """

    class Chapter:
        def __init__(self, title: str):
            self.title = title

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def get_title(self):
            return self.title

    class Book:
        def __init__(self, title: str, chapters: list[str]):
            self.title = title
            self.chapters = [Chapter(title) for title in chapters]

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def get_table_of_contents(self):
            toc = [self.title]
            for n, chapter in enumerate(self.chapters, start=1):
                toc.append(f"Глава {n}: {chapter.get_title()}")
            return "\n".join(toc)

    book_title = "Хоббит, или туда и обратно"
    chapter_titles = [
        "Стук в дверь",
        "Туда",
        "Приключения",
        "Обратно",
    ]

    book = Book(book_title, chapter_titles)
    ic(book)
    ic(book.get_table_of_contents())


def test_flexible_composition():
    """
    Задача 5: Гибкая композиция (Dependency Injection)
    """

    class Engine:
        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        @staticmethod
        def start(): ...

    class PetrolEngine(Engine):
        @staticmethod
        def start():
            return "Бензиновый двигатель запущен"

    class ElectricEngine(Engine):
        @staticmethod
        def start():
            return "Электрический двигатель активирован"

    class Car:
        def __init__(self, model: str, engine: Engine):
            self.model = model
            self.engine = engine

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

        def start_car(self):
            return self.engine.start()

    petrol_car = Car("Audi", PetrolEngine())
    ic(petrol_car)
    ic(petrol_car.start_car())
    electric_car = Car("Xiaomi", ElectricEngine())
    ic(electric_car)
    ic(electric_car.start_car())
