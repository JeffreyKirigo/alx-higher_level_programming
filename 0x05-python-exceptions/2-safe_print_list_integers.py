#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a
        list and only integers.

        Args:
            my_list (list): list to print elemnts from
            x (int): Number of elements to print

        Returns:
            The real number of integers printed
    """
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (n)
