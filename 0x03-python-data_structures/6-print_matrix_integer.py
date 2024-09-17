#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]] or len(matrix) == 0:
        print(end="$\n")
        return
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row), end="$\n")
