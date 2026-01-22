# library_system.py

class Book:
    """Base class representing a generic book with common attributes."""
    def __init__(self, title, author):
        """
        Initialize a Book with title and author.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class for EBooks, inheriting from Book."""
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook, calling the parent Book init and adding file_size.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size in KB.
        """
        super().__init__(title, author)  # Call parent's __init__ to set title and author
        self.file_size = file_size


class PrintBook(Book):
    """Derived class for PrintBooks, inheriting from Book."""
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook, calling the parent Book init and adding page_count.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages.
        """
        super().__init__(title, author)  # Call parent's __init__ to set title and author
        self.page_count = page_count


class Library:
    """Class demonstrating composition: A library 'has-a' collection of books."""
    def __init__(self):
        """Initialize an empty list to hold books."""
        self.books = []  # Composition: Library contains a list of Book instances

    def add_book(self, book):
        """
        Add a book (any subclass of Book) to the library's collection.
        
        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library, handling different types."""
        for book in self.books:
            if isinstance(book, EBook):
                # For EBooks, include file size
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                # For PrintBooks, include page count
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}.")
            else:
                # For generic Books, just show basics
                print(f"Book: {book.title} by {book.author}")