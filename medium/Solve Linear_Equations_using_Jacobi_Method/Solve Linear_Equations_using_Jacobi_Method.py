import numpy as np


# # Step 1
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    aii = np.diag(A).tolist()

    # To understand various ways of calculating non-diagonal elements, referred to this - https://stackoverflow.com/a/46736275/12346331
    m = np.array(A).shape[0]
    strided = np.lib.stride_tricks.as_strided
    s0, s1 = np.array(A).strides
    aij = strided(
        np.array(A).ravel()[1:], shape=(m - 1, m), strides=(s0 + s1, s1)
    ).reshape(m, -1)

    x = [0 for _ in range(len(b))]

    # Perform Jacobi iteration for n iterations
    for _ in range(n):
        new_x = x.copy()
        for i in range(m):
            sum_aij_xj = sum(A[i][j] * x[j] for j in range(m) if j != i)
            new_x[i] = round((1 / aii[i]) * (b[i] - sum_aij_xj), 4)
        x = new_x

    return x


# # Step 2
# def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
#     d_a = np.diag(A)
#     nda = A - np.diag(d_a)
#     x = np.zeros(len(b))
#     x_hold = np.zeros(len(b))
#     for _ in range(n):
#         for i in range(len(A)):
#             x_hold[i] = (1/d_a[i]) * (b[i] - sum(nda[i]*x))
#         x = x_hold.copy()
#     return np.round(x,4).tolist()

A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n = 2
print(solve_jacobi(A=A, b=b, n=n))  # type: ignore
