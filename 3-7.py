def is_transpose(matrix1, matrix2):

    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if rows1 != cols2 or cols1 != rows2:
        return False
    
    for i in range(rows1):
        for j in range(cols1):
            if matrix1[i][j] != matrix2[j][i]:
                return False
    
    return True

A = [
    [1, 2, 3],
    [4, 5, 6]
]

A_transpose = [
    [1, 4],
    [2, 5],
    [3, 6]
]

print(is_transpose(A, A_transpose))