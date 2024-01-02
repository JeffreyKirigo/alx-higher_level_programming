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
