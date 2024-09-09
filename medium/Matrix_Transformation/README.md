# Matrix Transformation (Medium) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Matrix Transformation](#learn-matrix-transformation)
- [Solutions](#solutions)
  - [Implementation](#implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Matrix Transformation](https://www.deep-ml.com/problem/Matrix%20Transformation)

Write a Python function that transforms a given matrix A using the operation $$T^{-1}AS$$, where T and S are invertible matrices. The function should first validate if the matrices T and S are invertible, and then perform the transformation.

## Example

```python
input: A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
output: [[0.5,1.5],[1.5,3.5]]
reasoning: The matrices T and S are used to transform matrix A by computing T^(-1)AS.
```

## Learn: Matrix Transformation

Transforming a matrix $$A$$ using the operation $$T^{-1}AS$$ involves several steps. This operation changes the basis of matrix $$A$$ using two invertible matrices $$T$$ and $$S$$. Given matrices $$A$$, $$T$$, and $$S$$:

1. **Check if $$T$$ and $$S$$ are invertible** by ensuring their determinants are non-zero.
2. **Compute the inverses** of $$T$$ and $$S$$, denoted as $$T^{-1}$$ and $$S^{-1}$$.
3. **Perform the matrix multiplication** to obtain the transformed matrix:

   $$A' = T^{-1}AS$$

### Example

If:

$$
A = \begin{pmatrix} 
1 & 2 \\ 
3 & 4 
\end{pmatrix}
$$

$$
T = \begin{pmatrix} 
2 & 0 \\ 
0 & 2 
\end{pmatrix}
$$

$$
S = \begin{pmatrix} 
1 & 1 \\ 
0 & 1 
\end{pmatrix}
$$

First, check that $$T$$ and $$S$$ are invertible:
- $$det(T) = 4 \neq 0$$
- $$det(S) = 1 \neq 0$$

Compute the inverses:

$$
T^{-1} = \begin{pmatrix} 
\frac{1}{2} & 0 \\ 
0 & \frac{1}{2} 
\end{pmatrix}
$$

Then, perform the transformation:

$$
A' = T^{-1}AS = \begin{pmatrix} 
\frac{1}{2} & 0 \\ 
0 & \frac{1}{2} 
\end{pmatrix} \begin{pmatrix} 
1 & 2 \\ 
3 & 4 
\end{pmatrix} \begin{pmatrix} 
1 & 1 \\ 
0 & 1 
\end{pmatrix} = \begin{pmatrix} 
0.5 & 1.5 \\ 
1.5 & 3.5 
\end{pmatrix}
$$

## Solutions

### Implementation

```python
import numpy as np

def transform_matrix(
    A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
) -> list[list[int | float]]:

    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        raise ValueError(
            "The determinant/s of the matrice/s equals 0; hence not invertible"
        )
    transformed_matrix = np.linalg.inv(T) @ A @ S
    return transformed_matrix  # type: ignore

A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]
print(transform_matrix(A=A, T=T, S=S))  # type: ignore
```

## Code Explanation

The `transform_matrix` function takes three parameters:
- `A`: The matrix to be transformed (list of lists)
- `T`: The first transformation matrix (list of lists)
- `S`: The second transformation matrix (list of lists)

The function implements the matrix transformation as follows:

1. It first checks if matrices `T` and `S` are invertible by calculating their determinants using `np.linalg.det()`. If either determinant is zero, it raises a `ValueError` with an appropriate message.

2. If both matrices are invertible, it performs the transformation using NumPy's matrix operations:
   - `np.linalg.inv(T)` computes the inverse of matrix `T`
   - The `@` operator is used for matrix multiplication
   - The operation `np.linalg.inv(T) @ A @ S` performs the transformation $$T^{-1}AS$$

3. The function returns the transformed matrix.

Note: The `# type: ignore` comments are used to suppress type checking warnings. In this case, they're used because the return type of NumPy operations might not strictly match the type hint `list[list[int | float]]`.

The commented out "Step 2" section is identical to the implemented "Step 1" section. It appears to be a duplicate of the same function, possibly left as a backup or for comparison purposes.

In the example usage, matrices `A`, `T`, and `S` are defined, and the `transform_matrix` function is called with these matrices as arguments. The result is then printed.

This implementation efficiently uses NumPy for matrix operations, which is particularly beneficial for larger matrices due to NumPy's optimized array operations.
