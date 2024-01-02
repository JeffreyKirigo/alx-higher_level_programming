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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
