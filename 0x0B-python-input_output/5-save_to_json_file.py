#!/usr/bin/python3
"""Define method"""
import json


def save_to_json_file(my_obj, filename):
    """Returns from json to python object"""
    message = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(message)
