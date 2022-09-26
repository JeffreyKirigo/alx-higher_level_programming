#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists.

    Args:
        my_list_1 (list): List with value for division
        my_list_2 (list): List with value for division
        list_length (int): n element for division

    Returns:
        new list (length = list_length) with all divisions
    """
    result_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)
    return (result_list)
