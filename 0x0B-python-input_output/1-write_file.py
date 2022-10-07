#!/usr/bin/python3
"""Define method"""


def write_file(filename="", text=""):
    """Write to file
    Args:
        filename (str): name of file
        text (str): Content to append to file
    """
    with open(filename, mode="w", encoding="utf-8") as m_file:
        return m_file.write(text)
