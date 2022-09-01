#!/usr/bin/python3

def uniq_add(my_list=[]):
    sums = 0
    unique_set = set(my_list)
    for x in unique_set:
        sums += x
    return sums
