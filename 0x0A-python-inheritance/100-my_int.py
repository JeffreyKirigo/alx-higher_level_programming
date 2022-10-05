#!/usr/bin/python3
"""Define class"""


class MyInt(int):
    """Override comparison operator"""

    def __eq__(self, value):
        """Overrides == operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator"""
        return self.real == value
