class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # False = available

    def check_out(self):
        """Try to check out this book"""
        if self._is_checked_out:
            return False  # already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return this book to the library"""
        if not self._is_checked_out:
            return False  # wasn't checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        """Returns True if book is currently available"""
        return not self._is_checked_out

    # Nice string representation (helps when printing)
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library"""
        if not isinstance(book, Book):
            print("Error: You can only add Book objects!")
            return
        self._books.append(book)

    def check_out_book(self, title):
        """Find book by title and check it out"""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'")
                    return
                else:
                    print(f"'{title}' is already checked out!")
                    return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        """Find book by title and return it"""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out!")
                    return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """Print all currently available books"""
        print("Available books:")
        available = [book for book in self._books if book.is_available()]
        
        if not available:
            print("   No books available at the moment.")
            return
            
        for book in available:
            print(f"   {book}")