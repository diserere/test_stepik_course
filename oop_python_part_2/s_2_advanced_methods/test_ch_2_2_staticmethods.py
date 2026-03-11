"""2.2 Статические методы (@staticmethod)"""

from icecream import ic


def test_staticmethod_format_email():
    """
    Задача 1: Простая утилита
    """

    class Formatter:
        @staticmethod
        def format_email(email: str):
            if isinstance(email, str) and "@" in email:
                return email.lower().strip()

    ic(Formatter.format_email("   My_EMAil@dot.coM"))
    ic(Formatter.format_email("   My_EMAil@DOT.coM   "))
    ic(Formatter.format_email("   \nMy_EMAil@dot.coM"))
    ic(Formatter.format_email("   My_EMAil @ DOT.coM   "))
    ic(Formatter.format_email("   \nMy_EMAil DOT.coM   "))
    ic(Formatter.format_email(["my_email@dot.com"]))  # pyright: ignore[reportArgumentType]
    ic(Formatter.format_email(123))  # pyright: ignore[reportArgumentType]


def test_staticmethod_library():
    """
    Задача 2: Класс-библиотека
    """

    class Validator:
        @staticmethod
        def is_positive(number: int | float):
            return isinstance(number, (int, float)) and number > 0

        @staticmethod
        def is_even(number: int):
            return isinstance(number, (int)) and number % 2 == 0

    ic(Validator.is_positive(-1))
    ic(Validator.is_positive(-10.5))
    ic(Validator.is_positive(0))
    ic(Validator.is_positive(0.1))
    ic(Validator.is_positive(1))
    ic(Validator.is_positive("1"))  # pyright: ignore[reportArgumentType]

    ic(Validator.is_even(-2))
    ic(Validator.is_even(-1))
    ic(Validator.is_even(-0.2))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(-0.1))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(0))
    ic(Validator.is_even(0.1))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(0.2))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even(1))
    ic(Validator.is_even(2))
    ic(Validator.is_even("1"))  # pyright: ignore[reportArgumentType]
    ic(Validator.is_even("2"))  # pyright: ignore[reportArgumentType]


def test_internal_static_method():
    """
    Задача 3: Использование статического метода внутри класса
    """

    class Circle:
        def __init__(self, radius) -> None:
            if self._is_valid_radius(radius):
                self.radius = radius
            else:
                raise ValueError("Некорректный радиус")

        @staticmethod
        def _is_valid_radius(radius):
            return isinstance(radius, (int, float)) and radius >= 0

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    ic(Circle(10))
    ic(Circle(1))
    ic(Circle(0.1))
    ic(Circle(1e-100))

    ic("Try: ic(Circle(0))")
    try:
        ic(Circle(0))
    except Exception as e:
        ic(e)

    ic("Try: ic(Circle(-1))")
    try:
        ic(Circle(-1))
    except Exception as e:
        ic(e)

    ic("Try: ic(Circle('1'))")
    try:
        ic(Circle("1"))
    except Exception as e:
        ic(e)


def test_different_methods():
    """
    Задача 4: Сравнение всех трех типов методов
    """

    class Counter:
        total_count = 0

        def __init__(self) -> None:
            self.instance_count = 0
            __class__.total_count += 1

        def increment(self):
            self.instance_count += 1

        @classmethod
        def get_total_count(cls):
            return cls.total_count

        @staticmethod
        def get_description():
            return "Это класс для подсчета."

        def __repr__(self):
            variables = [f"{k}={v!r}" for k, v in vars(self).items()]
            return f"{type(self).__name__}({', '.join(variables)})"

    ic(Counter.total_count)
    ic(Counter.get_total_count())

    ic("Try: counter_1 = Counter()")
    counter_1 = Counter()
    ic(counter_1)
    ic(counter_1.total_count)
    ic(counter_1.get_total_count())
    ic(counter_1.increment())
    ic(counter_1)

    ic(Counter.get_total_count())
    ic(Counter.total_count)

    ic("Try: counter_2 = Counter()")
    counter_2 = Counter()
    ic(counter_2)
    ic(counter_2.total_count)
    ic(counter_2.get_total_count())
    ic(counter_2.increment())
    ic(counter_2)

    ic(Counter.get_total_count())
    ic(Counter.total_count)

    ic(Counter.get_description())
    ic(counter_1.get_description())
    ic(counter_2.get_description())


def test_dateconverter():
    """
    Задача 5: Практический пример: DateConverter
    """

    class DateConverter:
        """Класс-библиотека для работы с датами."""

        DELIM_EUR = "."
        DELIM_ISO = "-"

        @staticmethod
        def to_iso_format(date_string: str):
            """Принимает дату в формате "ДД.ММ.ГГГГ" и возвращает ее в формате ISO "ГГГГ-ММ-ДД"."""
            if isinstance(date_string, str):
                dd, mm, yyyy = date_string.split(__class__.DELIM_EUR)
                return __class__.DELIM_ISO.join((yyyy.strip(), mm.strip(), dd.strip()))

        @staticmethod
        def from_iso_format(date_string: str):
            """Принимает дату в формате ISO "ГГГГ-ММ-ДД" и возвращает ее в формате "ДД.ММ.ГГГГ"."""
            if isinstance(date_string, str):
                yyyy, mm, dd = date_string.split(__class__.DELIM_ISO)
                return __class__.DELIM_EUR.join((dd.strip(), mm.strip(), yyyy.strip()))

    ic(DateConverter.to_iso_format("16.04.1986"))
    ic(DateConverter.from_iso_format(DateConverter.to_iso_format("16.04.1986")))

    ic(DateConverter.to_iso_format(" 16 .\t 04 . 1986 \n"))
    ic(DateConverter.from_iso_format("\f 2011- 03 \v- 11    \n\r"))
    ic('try: ic(DateConverter.to_iso_format("24.02-2022"))')
    try:
        ic(DateConverter.to_iso_format("24.02-2022"))
    except Exception as e:
        ic(e)

    ic('try: ic(DateConverter.from_iso_format("2022 02 24"))')
    try:
        ic(DateConverter.from_iso_format("2022 02 24"))
    except Exception as e:
        ic(e)

    ic('try: ic(DateConverter.to_iso_format("24.02..2022"))')
    try:
        ic(DateConverter.to_iso_format("24.02..2022"))
    except Exception as e:
        ic(e)
