#libary_system.py

class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book.
    """
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book.
    """
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """
    Class demonstrating composition.
    A Library contains and manages multiple Book objects.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}.")
            else:
                print(f"Book: {book.title} by {book.author}")
