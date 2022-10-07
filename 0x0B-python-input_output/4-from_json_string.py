#!/usr/bin/python3
"""Define method"""
import json


def from_json_string(my_str):
    """Returns from json to python object"""
    return json.loads(my_str)
