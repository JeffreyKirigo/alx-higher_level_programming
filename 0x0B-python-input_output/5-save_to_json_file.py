#!/usr/bin/python3
"""Define method"""
import json


def save_to_json_file(my_obj, filename):
    """Returns from json to python object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
