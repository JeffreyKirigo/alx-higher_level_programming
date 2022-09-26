#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

        Args:
            a (int): first value
            b (int): Second value

        Returns:
            The value of the division, otherwise: None
    """
    result = 0
    try:
        result = a / b
    except (ValueError, ZeroDivisionError, TypeError):
        result = None
        return (result)
    finally:
        print("Inside result: {}".format(result))
    return (result)
