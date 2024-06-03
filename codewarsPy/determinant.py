import numpy as np

def determinant(a):
    return round(np.linalg.det(np.matrix(a)))


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant(minor(matrix, 0, i))
        return det
    


def minor(matrix, row, col):
    new_matrix = []
    for i in range(len(matrix)):
        if i != row:
            new_matrix.append([])
            for j in range(len(matrix[i])):
                if j != col:
                    new_matrix[i - 1].append(matrix[i][j])
    return new_matrix

print(determinant([[1, 3, 3], [4, 5, 6], [7, 8, 9]]))