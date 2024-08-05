def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    l = []
    if mode == "row":
        for n in range(len(matrix)):
            sum = 0
            for i in matrix[n]:
                sum += i
            l.append(sum/len(matrix))

    elif mode == "column":
        for n in range(len(matrix[0])):
            sum = 0
            for i in [matrix[n]]:
                print(i)
                sum += i[0]
            # print(sum)
            l.append(sum/len(matrix[0]))

    return l

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = "column"

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# mode = 'row'

print(calculate_matrix_mean(matrix=matrix, mode=mode))
