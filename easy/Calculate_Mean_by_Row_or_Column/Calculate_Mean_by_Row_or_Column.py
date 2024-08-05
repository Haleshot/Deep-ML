# Step 1

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    l = []
    if mode == "row":
        for n in range(len(matrix)):
            sum = 0
            for i in matrix[n]:
                sum += i
            l.append(sum/len(matrix))

    elif mode == "column":
        for i in range(0, len(matrix)):
            sum = 0
            for j in range(0, len(matrix)):
                sum += matrix[j][i]
            l.append(sum/len(matrix[0]))
     
    return l

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mode = "column"

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'row'

print(calculate_matrix_mean(matrix=matrix, mode=mode))
