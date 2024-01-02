#!/usr/bin/python3
"""Define method"""


def is_same_class(a, types):
    """Checks if object(a) is an instance of type b

    Args:
        a (obj): obj  to compare
        b (types): types to compare to

    Returns:
        returns True if the object is exactly an instance of
        the specified class ; otherwise False
    """
    if type(a) == types:
        return True
    else:
        return False
