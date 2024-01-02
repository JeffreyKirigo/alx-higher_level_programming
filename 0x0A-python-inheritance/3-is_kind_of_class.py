#!/usr/bin/python3
"""Define method"""


def is_kind_of_class(obj, a_class):
    """ Same class or inherit from

    Args:
        obj: object to check instance of
        a_class: class to check instance of

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
