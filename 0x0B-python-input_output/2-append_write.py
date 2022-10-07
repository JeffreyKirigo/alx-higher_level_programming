#!/usr/bin/python3
"""Define method"""


def append_write(filename="", text=""):
    """Appends text to file
    Args:
        filename (str): file name
        text (str): text to append
    """
    with open(filename, "a", encoding="utf=8") as f:
        return f.write(text)
