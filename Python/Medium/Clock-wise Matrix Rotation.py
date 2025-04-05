def rotate(matrix):
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix