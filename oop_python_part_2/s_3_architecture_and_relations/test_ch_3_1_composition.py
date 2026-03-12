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


def test_():
    """
    docstring.
    """
    pass
