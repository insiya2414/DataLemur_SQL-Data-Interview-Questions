def can_rotate_to_match(mat, target):
    n = len(mat)
    
    # Function to rotate matrix 90 degrees clockwise
    def rotate_90_degrees(matrix):
        n = len(matrix)
        rotated = [[0 for _ in range(n)] for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                # In a 90-degree clockwise rotation:
                # row r, column c --> row c, column (n-1-r)
                rotated[c][n-1-r] = matrix[r][c]
                
        return rotated
    
    # Check if two matrices are equal
    def are_equal(mat1, mat2):
        for r in range(n):
            for c in range(n):
                if mat1[r][c] != mat2[r][c]:
                    return False
        return True
    
    # Try all possible rotations (0°, 90°, 180°, 270°)
    current = mat
    
    # Check 0° rotation (original matrix)
    if are_equal(current, target):
        return True
    
    # Check 90° rotation
    current = rotate_90_degrees(current)
    if are_equal(current, target):
        return True
    
    # Check 180° rotation
    current = rotate_90_degrees(current)
    if are_equal(current, target):
        return True
    
    # Check 270° rotation
    current = rotate_90_degrees(current)
    if are_equal(current, target):
        return True
    
    # If none of the rotations match, return False
    return False


