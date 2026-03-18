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
