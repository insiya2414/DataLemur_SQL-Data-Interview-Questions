def is_matrix_stripes(matrix):
    rows, cols = len(matrix), len(matrix[0])  # Get dimensions of the matrix

    for i in range(rows - 1):       # Loop through rows (except last)
        for j in range(cols - 1):   # Loop through columns (except last)
            if matrix[i][j] != matrix[i + 1][j + 1]:  # Compare with diagonal element
                return False  # Mismatch found, return False

    return True  # All diagonals match, return True