#!/usr/bin/python3
"""Define class"""


class MyList(list):
    """Inherits class list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
