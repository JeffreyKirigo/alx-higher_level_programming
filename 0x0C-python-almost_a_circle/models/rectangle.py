#!/usr/bin/python3
"""Define rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base class

    Attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Define init method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        self.__width = value

    @width.deleter
    def width(self):
        """deleter"""
        del self.__width

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        self.__height = value

    @height.deleter
    def height(self):
        """Deleter"""
        del self.__height
