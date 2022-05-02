def determinant(matrix):
    det = 0
    if len(matrix) == 1:
        return matrix[0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        sgn = 1
        for nm_index in range(len(matrix[0])):
            sub_matrix = [[*line[:nm_index], *line[nm_index+1:]] for line in matrix[1:]]
            det += sgn * matrix[0][nm_index] * determinant(sub_matrix)
            sgn *= -1
    return det


matrix = [[1, -2], [7, -5]]
print(determinant(matrix))
matrix = [[1, -2, 3, 3], [7, -5, 6, 11], [19, 8, 9, 27], [30, 40, 1, 0]]
print(determinant(matrix))
matrix = [[1, 2, 3], [4, 10, 6], [7, 8, 9]]
print(determinant(matrix))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(determinant(matrix))
matrix = [[1, -2, 3], [7, -5, 6], [19, 8, 9]]
print(determinant(matrix))
matrix = [1]
print(determinant(matrix))
