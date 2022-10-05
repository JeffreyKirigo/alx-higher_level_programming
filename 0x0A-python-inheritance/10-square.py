#!/usr/bin/python3
"""Class Definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for Base Geometry"""

    def __init__(self, size):
        """Initilization
        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of rectangle"""
        return self.__size**2

    def __str__(self):
        """Return a string rep of the class"""
        c_name = str(self.__class__.__name__)
        return "[{}] {}/{}".format(c_name, self.__size, self.__size)
