def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    l = []
    for i in matrix:
        l.append([j * scalar for j in i])
    return l


matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix=matrix, scalar=scalar))  # type: ignore


# import numpy as np

# matrix = [[1, 2], [3, 4]]
# scalar = 2

# print(np.multiply(matrix, scalar))
