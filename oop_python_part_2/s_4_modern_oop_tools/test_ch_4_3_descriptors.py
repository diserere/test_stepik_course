"""4.3 Дескрипторы: `__get__`, `__set__`, `__delete__`"""

from icecream import ic

from utils.utils import safe


class TestDescriptorProtocol:
    """Шаг 2: Протокол дескриптора: объяснение __get__, __set__ и __delete__."""

    def test_custom_get_descriptor(self):
        """
        1. __get__(self, instance, owner) — Перехват чтения.

        Сигнатура:
            def __get__(self, instance, owner):
                - self: Это сам экземпляр дескриптора (в нашем примере — Owner.attr).
                - instance: Это экземпляр класса-владельца, через который идет обращение. В нашем примере — obj.
                Если обращение идет через сам класс (Owner.attr), то instance будет None.
                - owner: Это сам класс-владелец. В нашем примере — Owner.
        """

        class GetDescriptor:
            def __get__(self, instance, owner):
                print("Вызван __get__:")
                print(f"  - self:     {self}")
                print(f"  - instance: {instance}")
                print(f"  - owner:    {owner}")
                return "Значение из __get__"

        class Owner:
            attr = GetDescriptor()

        ic("Create obj = Owner()")
        obj = Owner()
        ic(obj)

        with safe():
            ic("Do: ic(obj.attr)")
            ic(obj.attr)
            ic(obj.__dict__)
            ic('Do:" obj.attr = "Установлено через __set__"')
            obj.attr = "Установлено через __set__"  # pyright: ignore[reportAttributeAccessIssue]
            ic(obj.attr)

    def test_custom_set_descriptor(self):
        """
        2. __set__(self, instance, value) — Перехват записи

        Сигнатура:
            def __set__(self, instance, value):
                - self: Экземпляр дескриптора.
                - instance: Экземпляр класса-владельца (obj).
                - value: Значение, которое пытаются присвоить. В нашем примере — 10.
        """

        class SetDescriptor:
            def __set__(self, instance, value):
                print("Вызван __set__:")
                print(f"  - instance: {instance}")
                print(f"  - value:    {value}")
                # Где-то сохраняем это значение, например, во внутреннем словаре
                instance.__dict__["internal_attr"] = value

        class Owner:
            attr = SetDescriptor()

        ic("Create obj = Owner()")
        obj = Owner()
        ic(obj)
        ic(obj.attr)
        ic(obj.__dict__)
        with safe():
            ic('Do: obj.attr = "Новое значение"')
            obj.attr = "Новое значение"
            ic(obj)
            ic(obj.attr)
            ic(obj.__dict__)
            ic(obj.internal_attr)  # pyright: ignore[reportAttributeAccessIssue]

    def test_custom_delete_descriptor(self):
        """
        3. __delete__(self, instance) — Перехват удаления

        Сигнатура:
            def __delete__(self, instance):
                - self: Экземпляр дескриптора.
                - instance: Экземпляр класса-владельца (obj).
        """

        class DeleteDescriptor:
            def __delete__(self, instance):
                print("Вызван __delete__:")
                print(f"  - instance: {instance}")
                print("...атрибут удален (имитация).")

        class Owner:
            attr = DeleteDescriptor()

        obj = Owner()
        ic(obj)
        ic(obj.attr)
        ic(obj.__dict__)

        with safe():
            ic("Do: del obj.attr")
            del obj.attr
            ic(obj)
            ic(obj.attr)
            ic(obj.__dict__)


class TestCreateDescriptorValidator:
    """Шаг 3: Пишем свой собственный дескриптор-валидатор."""

    def test_create_descriptor_validator(self):
        """Задача:

        Создать дескриптор NonNegative, который можно будет применить к любому атрибуту в любом классе.
        Этот дескриптор должен гарантировать, что атрибуту нельзя присвоить отрицательное число.
        """

        ic("Init class NonNegative")

        class NonNegative:
            """Дескриптор, который не позволяет установить отрицательное значение."""

            def __set_name__(self, owner, name):
                # Этот "бонусный" магический метод вызывается при создании класса.
                # Он позволяет дескриптору "узнать" имя атрибута, которому он присвоен.
                print(f"  - In __set_name__: self: {self}, owner: {owner}, name: {name}")
                self.private_name = "_" + name

            def __get__(self, instance, owner):
                print(f"  - In __get__: self: {self}, instance: {instance}, owner: {owner}")
                # Получаем значение из __dict__ экземпляра по нашему приватному имени
                return getattr(instance, self.private_name)

            def __set__(self, instance, value):
                print(f"  - In __set__: self: {self}, instance: {instance}, value: {value}")
                # --- Вот наша логика валидации ---
                if value < 0:
                    raise ValueError("Значение не может быть отрицательным.")

                # Сохраняем значение в __dict__ экземпляра под приватным именем
                setattr(instance, self.private_name, value)

        ic("Init class Product")

        class Product:
            price = NonNegative()
            quantity = NonNegative()

            def __init__(self, name, price, quantity):
                self.name = name
                self.price = price
                self.quantity = quantity

            def __repr__(self):
                variables = [f"{k}={v!r}" for k, v in self.__dict__.items()]
                return f"{type(self).__name__}({', '.join(variables)})"

        ic("Create valid apple:")
        with safe():
            apple = Product("Apple", 10, 5)
            ic(apple)
            ic(apple.__dict__)
            ic(apple.price)
            ic(apple.quantity)

        ic("Try to set valid price:")
        with safe():
            apple.price = 100
            ic(apple)
            ic(apple.price)

        ic("Try to set negative price:")
        with safe():
            apple.price = -10

        ic("Create invalid banana:")
        with safe():
            banana = Product("Banana", 10, -10)
            ic(banana)


def test_readonly_descriptor():
    """
    Задача 1: Дескриптор для константы (только для чтения)
    """

    class ConstantDescriptor:
        def __init__(self, value):
            self.value = value

        def __get__(self, instance, owner):
            print(f"  - In __get__: self: {self}, instance: {instance}, owner: {owner}")
            return self.value

        def __set__(self, instance, value):
            print(f"  - In __set__: self: {self}, instance: {instance}, value: {value}")
            raise AttributeError("Attribute is read-only")

    class MyClass:
        PI = ConstantDescriptor(3.14159)
        FI = ConstantDescriptor(1.61803)

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in self.__dict__.items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    ic("Create instance:")
    my_cls = MyClass()
    ic(my_cls)
    ic(my_cls.PI)
    ic(my_cls.FI)
    ic(my_cls.__dict__)
    ic("---")

    ic("Try to set attr PI:")
    with safe():
        my_cls.PI = 1.6
    ic(my_cls)
    ic(my_cls.PI)
    ic("---")

    ic("Try to set attr FI:")
    with safe():
        my_cls.FI = 2.7
    ic(my_cls)
    ic(my_cls.FI)
    ic("---")

    ic("Try to delete attr:")
    with safe():
        del my_cls.PI
    ic(my_cls)
    with safe():
        ic(my_cls.PI)
    ic("---")

    ic("Test class:")
    ic(MyClass)
    ic(MyClass.PI)
    # ic(MyClass.__dict__)
    ic("Try to set attr in class:")
    with safe():
        MyClass.PI = 1.6
        ic(MyClass)
        ic(MyClass.PI)
        # ic(MyClass.__dict__)
    ic("---")


def test_():
    """
    docstring.
    """
    pass
