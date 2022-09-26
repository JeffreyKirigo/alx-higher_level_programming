#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer

    Args:
        value : Takes any value

    Returns:
        True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
