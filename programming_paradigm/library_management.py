class Book:
    def __init__(self, title, author):
        self.title = title                  # Public attribute
        self.author = author                # Public attribute
        self._is_checked_out = False         # Private attribute

    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available"""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []                    # Private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library"""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return

    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """List all available books"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
