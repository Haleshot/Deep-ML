def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    print("rows ", len(matrix), " columns", len(matrix[0]))
    l = []
    if mode == "row":
        sum = 0
        for i in matrix:
            sum += i[0]
            # sum = sum / len(matrix)

    elif mode == "column":
        sum = 0
        for i in matrix:
            sum += i[0]
            l.append(sum)
            # sum = sum / len(matrix[0])
    return l

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = "column"
print(calculate_matrix_mean(matrix=matrix, mode=mode))