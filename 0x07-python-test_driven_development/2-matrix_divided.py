#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(err_msg)
    for row in matrix:
        if type(row) != list:
            raise TypeError(err_msg)
        for num in row:
            if type(num) not in (int, float):
                raise TypeError(err_msg)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
