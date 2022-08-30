#!/usr/bin/python3

def no_c(my_string):
    str_cp = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(str_cp))
