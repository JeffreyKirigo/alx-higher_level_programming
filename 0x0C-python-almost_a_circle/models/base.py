#!/usr/bin/python3
"""Define base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilization of class
        Args:
            id (int): an identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
