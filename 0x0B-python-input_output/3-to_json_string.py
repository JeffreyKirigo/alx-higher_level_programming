#!/usr/bin/python3
import json

"""Define method"""


def to_json_string(my_obj):
    """Returns json rep of an object
    Args:
        my_obj: object for json representation
    """
    return json.dumps(my_obj)
