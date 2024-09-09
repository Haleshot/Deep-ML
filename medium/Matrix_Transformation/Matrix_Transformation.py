import numpy as np


def transform_matrix(
    A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
) -> list[list[int | float]]:
    transformed_matrix = np.linalg.inv(T) @ A @ S
    return transformed_matrix

A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]
print(transform_matrix(A=A, T=T, S=S))