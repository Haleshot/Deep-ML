# Scalar Multiplication of a Matrix (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Scalar Multiplication of a Matrix](#learn-scalar-multiplication-of-a-matrix)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Scalar Multiplication of a Matrix](https://www.deep-ml.com/problem/Scalar%20Multiplication%20of%20a%20Matrix)

Write a Python function that performs scalar multiplication on a matrix. The function should take a matrix (represented as a list of lists) and a scalar value as input, and return the resulting matrix after scalar multiplication.

## Example

```python
input: matrix = [[1, 2], [3, 4]], scalar = 2
output: [[2, 4], [6, 8]]
reasoning: Each element of the matrix is multiplied by the scalar.
```

## Learn: Scalar Multiplication of a Matrix

When a matrix $A$ is multiplied by a scalar $k$, the operation is defined as multiplying each element of $A$ by $k$. Given a matrix $A$:

$$
A = \begin{pmatrix} 
a_{11} & a_{12} \\ 
a_{21} & a_{22} 
\end{pmatrix}
$$

And a scalar $k$, the result of the scalar multiplication $kA$ is:

$$
kA = \begin{pmatrix} 
ka_{11} & ka_{12} \\ 
ka_{21} & ka_{22} 
\end{pmatrix}
$$

This operation scales the matrix by $k$ without changing its dimension or the relative proportion of its elements.

## Solutions

### Custom Implementation

```python
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    l = []
    for i in matrix:
        l.append([j * scalar for j in i])
    return l

matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix=matrix, scalar=scalar))
```

### NumPy Implementation

```python
import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return (np.multiply(matrix, scalar))

# Usage remains the same as the custom implementation
```

## Code Explanation

The custom implementation of `scalar_multiply` function takes two parameters:

- `matrix`: a 2D list representing the input matrix
- `scalar`: an integer or float value to multiply the matrix with

The function works as follows:

1. It initializes an empty list `l` to store the result.
2. It iterates through each row `i` of the input matrix.
3. For each row, it creates a new list comprehension `[j * scalar for j in i]` which multiplies each element `j` in the row by the scalar value.
4. The resulting row is appended to the list `l`.
5. Finally, it returns the list `l` containing the scalar-multiplied matrix.

This implementation is a straightforward and intuitive approach to scalar multiplication of a matrix. It directly applies the mathematical definition of scalar multiplication by iterating through each element of the matrix and multiplying it by the scalar value.

The NumPy implementation, on the other hand, utilizes the built-in `np.multiply()` function from the NumPy library. This method is more concise and potentially more efficient, especially for larger matrices, as it leverages NumPy's optimized array operations.

Both implementations will produce the same result, but the NumPy version may be preferred in scenarios where performance is critical or when working with larger datasets that are already in NumPy array format.
