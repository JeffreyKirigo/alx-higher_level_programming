#!/usr/bin/python3
"""Define Function"""


def say_my_name(first_name, last_name=""):
    """Prints the named parameters

    Args:
        first_name (str): first name as string
        last_name (str): last name as string

    Returns:
        Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
