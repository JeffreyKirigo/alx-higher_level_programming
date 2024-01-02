#!/usr/bin/python3
"""Class Definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for Base Geometry"""

    def __init__(self, width, height):
        """Initilization
        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string rep of the class"""
        c_name = str(self.__class__.__name__)
        return "[{}] {}/{}".format(c_name, self.__width, self.__height)
