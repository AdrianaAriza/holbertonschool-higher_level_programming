#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    a = list(map(lambda i: list(map(lambda j: j*j, i)), matrix))
    return a
