# # Step 1


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    l = []
    if mode == "row":
        for n in range(len(matrix)):
            sum = 0
            for i in matrix[n]:
                sum += i
            l.append(sum / len(matrix))

    elif mode == "column":
        for i in range(0, len(matrix)):
            sum = 0
            for j in range(0, len(matrix)):
                sum += matrix[j][i]
            l.append(sum / len(matrix[0]))

    return l


# # Step 2
# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
#     if mode == "row":
#         return [sum(row) / len (row) for row in matrix]
#     elif mode == "column":
#         return [sum(col) / len(matrix) for col in zip(*matrix)]
#     else:
#         raise ValueError("Mode must be of type 'row' or 'column' ")

# # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # mode = "column"

# # Step 3
# import numpy as np
# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
#     if mode == "row":
#         return np.array(np.sum(matrix, axis=0) // len(matrix)).tolist()
#     elif mode == "column":
#         return np.array(np.sum(matrix, axis=1) // len(matrix[0])).tolist()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = "column"

print(calculate_matrix_mean(matrix=matrix, mode=mode))  # type: ignore
