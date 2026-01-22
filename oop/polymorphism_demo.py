import math


class Shape:
    """
    Base class representing a general shape.
    """
    def area(self):
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

