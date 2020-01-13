#!/usr/bin/python3
def matrix_divided(matrix, div):
    r = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TyperError("r")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("r")
    for j in i:
        if not isinstance(j, int) and not isinstance(j, float):
            raise TypeError("r")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(i / div, 2) for i in j] for j in matrix])
