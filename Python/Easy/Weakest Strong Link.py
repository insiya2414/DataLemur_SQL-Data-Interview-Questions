def weakest_Strong_Link(strength):
    rows, cols = len(strength), len(strength[0])

    # Find the weakest link in each row
    row_min = {i: min(strength[i]) for i in range(rows)}

    # Find the strongest link in each column
    col_max = {j: max(strength[i][j] for i in range(rows)) for j in range(cols)}

    # Check for a Weakest Strong Link
    for i in range(rows):
        for j in range(cols):
            if strength[i][j] == row_min[i] and strength[i][j] == col_max[j]:
                return strength[i][j]

    return -1  # No Weakest Strong Link found