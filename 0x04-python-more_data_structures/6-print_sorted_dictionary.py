#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keyss = sorted(a_dictionary.keys())
    for x in keyss:
        print("{}: {}".format(x, a_dictionary[x]))
