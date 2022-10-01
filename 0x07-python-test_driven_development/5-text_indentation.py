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
    checker = False
    if type(text) != str:
        raise TypeError("text must be a string")

    for x in text:
        if not checker:
            print(x, end="")
            if x in special:
                checker = True
                print("\n")
        else:
            if x == " ":
                checker = True
                continue
            else:
                print(x, end="")
                checker = False
