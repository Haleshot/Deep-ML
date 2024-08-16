# # Step 1
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    l = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return l


a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(a=a))  # type: ignore


# # Step 2
# def transpose_matrix(a : list[list[int | float]]) -> list[list[int | float]]:
#     matrix_a = list(zip(*a))
#     return [list(a) for a in matrix_a]

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transpose_matrix(a=a))


# # Step 3
# import numpy as np

# def transpose_matrix(a : list[list[int | float]]) -> list[list[int | float]]:
#     return np.matrix_transpose(a)

# a = [[1, 2, 3], [4, 5, 6]]
# print(transpose_matrix(a=a))
