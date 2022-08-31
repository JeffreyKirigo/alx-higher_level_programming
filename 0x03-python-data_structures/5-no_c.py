#!/usr/bin/python3

def no_c(my_string):
    str_cp = my_string.translate({ord(x): None for x in 'cC'})
    return str_cp
