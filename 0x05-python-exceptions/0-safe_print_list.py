#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print n elements of a list

    Args:
        my_list (list): List to print elements from
        x (int): Number of elements to print

    Returns:
        Number of element printed
    """
    n = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            n += 1
        except IndexError:
            break
    print("")
    return (n)
