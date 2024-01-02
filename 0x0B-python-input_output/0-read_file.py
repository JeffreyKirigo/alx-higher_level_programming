#!/usr/bin/python3
"""Define method"""


def read_file(filename=""):
    """Reads a file and prints to stdout
    Args:
        filename (str): name of file to read
    """
    with open(filename, encoding="utf-8") as m_file:
        print(m_file.read(), end="")
