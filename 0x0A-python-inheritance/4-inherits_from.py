#!/usr/bin/python3
"""Define method to check if sub class of x"""


def inherits_from(obj, a_class):
    """Only sub class of

    Args:
        obj: object to check
        a_class: sub class to check against

    Returns:
        True if the object is an instance of a
        class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
