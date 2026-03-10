from icecream import ic  # noqa: F401



def test_magic_str():
    """
    1.3 Строковое представление: __str__ и __repr__
    
    Задача 1: Реализация __str__
    """
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return f'"{self.title}" автора {self.author}'

    book = Book("1984", "George Orwell")

    ic(book)
    print(book)
