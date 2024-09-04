import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    aii = np.diag(A).tolist()
    # print(aii)
    # return x


A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n = 2
print(solve_jacobi(A=A, b=b, n=n))
