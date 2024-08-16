# Step 1
import numpy as np


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    return np.dot(np.linalg.inv(C), B)  # type: ignore


B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

C = [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]]

print(transform_basis(B=B, C=C))
