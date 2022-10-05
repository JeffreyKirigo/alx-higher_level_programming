#!/usr/bin/python3
"""Class Definition"""


class BaseGeometry:
    """Class for Base Geometry"""

    def __init__(self):
        """Initilization

        Args:
            self: self referential

        Returns:
            Nothing
        """
        pass

    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
