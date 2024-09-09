import numpy as np


# # Step 1
def transform_matrix(
    A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
) -> list[list[int | float]]:

    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        raise ValueError(
            "The determinant/s of the matrice/s equals 0; hence not invertible"
        )
    transformed_matrix = np.linalg.inv(T) @ A @ S
    return transformed_matrix  # type: ignore


# # Step 2
# def transform_matrix(
#     A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
# ) -> list[list[int | float]]:

#     if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
#         raise ValueError(
#             "The determinant/s of the matrice/s equals 0; hence not invertible"
#         )
#     transformed_matrix = np.linalg.inv(T) @ A @ S
#     return transformed_matrix # type: ignore


A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]
print(transform_matrix(A=A, T=T, S=S))  # type: ignore
