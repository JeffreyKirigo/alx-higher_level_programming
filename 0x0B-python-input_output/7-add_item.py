#!/usr/bin/python3
"""Define Method load,add,save"""
import sys

if __name__ == "__main__":
    load_from_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        list_items = load_from_file(filename)
    except FileNotFoundError:
        list_items = []
    list_items.extend(sys.argv[1:])
    save_to_json_file(list_items, filename)
