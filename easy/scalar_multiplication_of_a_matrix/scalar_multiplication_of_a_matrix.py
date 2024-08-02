def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[j * scalar] for i in matrix for j in i]

matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix=matrix, scalar=scalar))

# import numpy as np

# matrix = [[1, 2], [3, 4]]
# scalar = 2

# print(np.multiply(matrix, scalar))
