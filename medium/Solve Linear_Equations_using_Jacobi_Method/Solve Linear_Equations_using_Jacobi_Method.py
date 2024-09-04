import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    aii = np.diag(A).tolist()
    # print(aii)
    m = np.array(A).shape[0]
    strided = np.lib.stride_tricks.as_strided
    s0, s1 = np.array(A).strides
    aij = strided(
        np.array(A).ravel()[1:], shape=(m - 1, m), strides=(s0 + s1, s1)
    ).reshape(m, -1)
    # print(aij)


A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n = 2
print(solve_jacobi(A=A, b=b, n=n))  # type: ignore
