#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(len(row))] for row in matrix]

    # Iterate over each element in the matrix and compute the square value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    # Return the resulting matrix
    return result
