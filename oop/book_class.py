class Book:
    """
    A simple class that represents a book with title, author, and publication year.
    Demonstrates the use of several important Python magic methods (dunder methods).
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor - called automatically when we create a new Book object.
        
        Args:
            title (str): The title of the book
            author (str): The name of the author
            year (int): The year the book was published
        """
        self.title = title
        self.author = author
        self.year = year
        
        # Optional: you could add validation here in real code
        # if not isinstance(year, int) or year < 0:
        #     raise ValueError("Year must be a positive integer")
    
    
    def __del__(self):
        """
        Destructor - called automatically when the object is being destroyed
        (usually when it goes out of scope or when del is used).
        """
        print(f"Deleting {self.title}")
    
    
    def __str__(self):
        """
        Human-friendly string representation.
        This is what gets called when you do: print(book)
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    
    def __repr__(self):
        """
        Official / developer-friendly representation.
        Goal: should return a string that (ideally) can be used to recreate the object.
        This is what you see when you just type the object name in the REPL
        or when you use repr(book).
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"