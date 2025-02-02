""" 
В данном проекте использованы три паттерна: Factory Method, Observer и Command.

Factory Method применяется в BookFactory для создания объектов книг, 
что упрощает процесс добавления новых типов книг в будущем. 

Observer реализован через Logger и Librarian, где логгер отслеживает 
и фиксирует действия библиотекаря, записывая информацию о добавлении и удалении книг. 

Command используется в AddBookCommand, RemoveBookCommand и Reader, 
где команды инкапсулируют операции с библиотекой, а Reader выступает в роли Invoker, 
вызывая команды по необходимости.

Этот набор паттернов делает код гибким, расширяемым и удобным для поддержки, 
позволяя легко добавлять новые книги, 
логировать события и управлять командами без изменения основной логики.
"""


from abc import ABC, abstractmethod

class Book:
    """
    Представляет книгу в библиотеке.
    """
    def __init__(self, title, author):
        """
        Инициализирует книгу (title) с автором (author).
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Возвращает строковое представление книги.
        """
        return f'"{self.title}" - {self.author}'


class BookFactory:
    """
    Фабрика для создания книг.
    """
    def create_book(self, title, author):
        """
        Создает книгу (title) с автором (author).
        """
        return Book(title, author)


class Logger:
    """
    Логгер для записи действий в библиотеке.
    """
    def update(self, message):
        """
        Записывает сообщение (message) в лог.
        """
        print(f"Лог: {message}")


class Librarian:
    """
    Библиотекарь, управляющий книгами и логирующий действия.
    """
    def __init__(self, logger):
        """
        Инициализирует библиотекаря с логгером (logger).
        """
        self.logger = logger

    def add_book(self, book):
        """
        Добавляет книгу (book) в библиотеку и логирует действие.
        """
        self.logger.update(f"Добавлена книга: {book}")

    def remove_book(self, book):
        """
        Удаляет книгу (book) из библиотеки и логирует действие.
        """
        self.logger.update(f"Удалена книга: {book}")


class Command(ABC):
    """
    Абстрактный класс для команд, выполняющих действия с книгами.
    """
    @abstractmethod
    def execute(self):
        """
        Выполняет команду.
        """
        pass


class AddBookCommand(Command):
    """
    Команда для добавления книги в библиотеку.
    """
    def __init__(self, library, book):
        """
        Инициализирует команду для добавления книги (book) в библиотеку (library).
        """
        self.library = library
        self.book = book

    def execute(self):
        """
        Добавляет книгу (book) в библиотеку (library).
        """
        self.library.add_book(self.book)


class RemoveBookCommand(Command):
    """
    Команда для удаления книги из библиотеки.
    """
    def __init__(self, library, book):
        """
        Инициализирует команду для удаления книги (book) из библиотеки (library).
        """
        self.library = library
        self.book = book

    def execute(self):
        """
        Удаляет книгу (book) из библиотеки (library).
        """
        self.library.remove_book(self.book)


class Reader:
    """
    Читатель, который вызывает команды для работы с книгами.
    """
    def __init__(self, library, librarian):
        """
        Инициализирует читателя с библиотекой (library) и библиотекарем (librarian).
        """
        self.library = library
        self.librarian = librarian

    def request_add_book(self, book):
        """
        Запрашивает добавление книги (book) в библиотеку.
        """
        add_command = AddBookCommand(self.library, book)
        add_command.execute()
        self.librarian.add_book(book)

    def request_remove_book(self, book):
        """
        Запрашивает удаление книги (book) из библиотеки.
        """
        remove_command = RemoveBookCommand(self.library, book)
        remove_command.execute()
        self.librarian.remove_book(book)


class Library:
    """
    Библиотека, в которой хранятся книги.
    """
    def __init__(self):
        """
        Инициализирует пустую библиотеку.
        """
        self.books = []

    def add_book(self, book):
        """
        Добавляет книгу (book) в библиотеку.
        """
        self.books.append(book)

    def remove_book(self, book):
        """
        Удаляет книгу (book) из библиотеки.
        """
        self.books.remove(book)

    def show_books(self):
        """
        Выводит список всех книг в библиотеке.
        """
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            for book in self.books:
                print(book)

if __name__ == "__main__":
    # Тестирование системы
    logger = Logger()
    library = Library()
    librarian = Librarian(logger)
    reader = Reader(library, librarian)
    book_factory = BookFactory()
    
    book1 = book_factory.create_book("1984", "Джордж Оруэлл")
    book2 = book_factory.create_book("1963", "Удивительный Человек-паук")
    
    reader.request_add_book(book1)
    reader.request_add_book(book2)

    print("\nКниги в библиотеке после добавления:")
    library.show_books()

    reader.request_remove_book(book1)
    
    book3 = book_factory.create_book("1869", "Война и мир")
    reader.request_add_book(book3)

    print("\nКниги в библиотеке после удаления:")
    library.show_books()

