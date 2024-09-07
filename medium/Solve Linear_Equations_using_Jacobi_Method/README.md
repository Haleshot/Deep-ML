# Solve Linear Equations using Jacobi Method (Medium) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Solving Linear Equations Using the Jacobi Method](#learn-solving-linear-equations-using-the-jacobi-method)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Solve Linear Equations using Jacobi Method](https://www.deep-ml.com/problem/Solve%20Linear%20Equations%20using%20Jacobi%20Method)

Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. The function should iterate 10 times, rounding each intermediate solution to four decimal places, and return the approximate solution x.

## Example

```python
input: A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]], b = [-1, 2, 3], n=2
output: [0.146, 0.2032, -0.5175]
reasoning: The Jacobi method iteratively solves each equation for x[i] using the formula x[i] = (1/a_ii) * (b[i] - sum(a_ij * x[j] for j != i)), where a_ii is the diagonal element of A and a_ij are the off-diagonal elements.
```

## Learn: Solving Linear Equations Using the Jacobi Method

The Jacobi method is an iterative algorithm used for solving a system of linear equations. This method is particularly useful for large systems where direct methods like Gaussian elimination are computationally expensive.

### Algorithm Overview

For a system of equations represented by $$Ax = b$$, where $$A$$ is a matrix and $$x$$ and $$b$$ are vectors, the Jacobi method involves the following steps:

1. **Initialization**: Start with an initial guess for $$x$$.
2. **Iteration**: For each equation $$i$$, update $$x_i$$ using:

   $$x_i = \frac{1}{a_{ii}} (b_i - \sum_{j \neq i} a_{ij} x_j)$$

   where $$a_{ii}$$ are the diagonal elements of $$A$$, and $$a_{ij}$$ are the off-diagonal elements.

3. **Convergence**: Repeat the iteration until the changes in $$x$$ are below a certain tolerance or until a maximum number of iterations is reached.

This method assumes that all diagonal elements of $$A$$ are non-zero and that the matrix is diagonally dominant or properly conditioned for convergence.

### Practical Considerations

- The method may not converge for all matrices.
- Choosing a good initial guess can improve convergence.
- Diagonal dominance of $$A$$ ensures convergence of the Jacobi method.

## Solutions

### Custom Implementation

```python
import numpy as np

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

A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n = 2
print(solve_jacobi(A=A, b=b, n=n))  # type: ignore
```

### NumPy Implementation

```python
import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    d_a = np.diag(A)
    nda = A - np.diag(d_a)
    x = np.zeros(len(b))
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(len(A)):
            x_hold[i] = (1/d_a[i]) * (b[i] - sum(nda[i]*x))
        x = x_hold.copy()
    return np.round(x,4).tolist()

# Usage remains the same as the custom implementation
```

## Code Explanation

### Custom Implementation

1. The function `solve_jacobi` takes three parameters:
   - `A`: The coefficient matrix (numpy array)
   - `b`: The constant vector (numpy array)
   - `n`: The number of iterations

2. `aii = np.diag(A).tolist()`: Extracts the diagonal elements of matrix A and converts them to a list.

3. The commented section calculates non-diagonal elements using numpy's `as_strided` function. This is an advanced technique for efficient array manipulation:
   ```python
   m = np.array(A).shape[0]
   strided = np.lib.stride_tricks.as_strided
   s0, s1 = np.array(A).strides
   aij = strided(
       np.array(A).ravel()[1:], shape=(m - 1, m), strides=(s0 + s1, s1)
   ).reshape(m, -1)
   ```
   This creates a view of the non-diagonal elements, which can be useful for optimization in larger matrices.

4. `x = [0 for _ in range(len(b))]`: Initializes the solution vector with zeros.

5. The main iteration loop:
   - Iterates `n` times
   - Creates a copy of `x` for updating
   - For each equation, calculates the new value of `x[i]` using the Jacobi method formula
   - Rounds each value to 4 decimal places

6. Returns the final solution vector.

### NumPy Implementation

1. `d_a = np.diag(A)`: Extracts the diagonal elements of A.
2. `nda = A - np.diag(d_a)`: Calculates the non-diagonal elements by subtracting the diagonal from A.
3. Initializes `x` and `x_hold` as zero vectors.
4. The main iteration loop:
   - Updates each `x[i]` using vectorized operations
   - Copies `x_hold` to `x` after each iteration
5. Returns the rounded solution vector.

Both implementations follow the Jacobi method algorithm, but the NumPy implementation uses more numpy operations, which can be more efficient for larger matrices. The custom implementation is more explicit in its calculations, which can be helpful for understanding the process.

The code then demonstrates the usage of the function with a sample 3x3 system of equations, iterating twice (`n=2`).
