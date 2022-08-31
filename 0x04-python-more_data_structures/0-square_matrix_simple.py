#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[y**2 for y in x] for x in matrix]
    return new_mat
