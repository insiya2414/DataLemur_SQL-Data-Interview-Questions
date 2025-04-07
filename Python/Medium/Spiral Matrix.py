def spiral_order(matrix):
    def rotate_image(matrix):
        columns_dict = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j not in columns_dict:
                    # Initialize the list if the key doesn't exist
                    columns_dict[j] = []  
                columns_dict[j].append(matrix[i][j])

        # Create the rotated matrix by reversing each column
        rotated_matrix = []
        for col in range(len(matrix[0])):
        	# Reverse the column
            rotated_matrix.append(columns_dict[col][::-1])  

        return rotated_matrix

    ans = []
    while matrix:
        ans += matrix[0]  # Add the first row to the answer
        matrix = matrix[1:]  # Remove the first row

        if not matrix:
            break  # If no more rows, break the loop

        '''
        Rotate the matrix counterclockwise 
        (by rotating clockwise 3 times)
        '''
        for _ in range(3):
            matrix = rotate_image(matrix)

    return ans