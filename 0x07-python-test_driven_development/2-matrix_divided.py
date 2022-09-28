#!/usr/bin/python3
"""Matrix division function."""


def matrix_divided(matrix, div):
    """Divide elemnts of a matrix by div.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Returns:
        New matrix with results from division
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(item / div, 2) for item in subl] for subl in matrix])
