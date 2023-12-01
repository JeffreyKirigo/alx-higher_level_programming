#!/usr/bin/python3
"""Define print square function"""


def print_square(size):
    """Prints square of size n

    Args:
        size (int): Size of square

    Returns:
        Nothing
    """
    symbol = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            [print("{}".format(symbol), end="") for k in range(size)]
            print()
