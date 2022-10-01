#!/usr/bin/python3
"""Define text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines

    Args:
        text (str): Text to be indented

    Returns:
        Nothing
    """
    special = [".", "?", ":"]

    if type(text) != str:
        raise TypeError("text must be a string")
    for x in range(len(text)):
        print(text[x], end="")
        if text[x] in special:
            print("\n\n", end="")
