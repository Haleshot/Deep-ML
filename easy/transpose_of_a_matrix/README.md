# Transpose of a Matrix (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Transpose of a Matrix](#learn-transpose-of-a-matrix)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [Alternative Custom Implementation](#alternative-custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Transpose of a Matrix](https://www.deep-ml.com/problem/Transpose%20of%20a%20Matrix)

Write a Python function that computes the transpose of a given matrix.

## Example

```python
input: a = [[1, 2, 3], [4, 5, 6]]
output: [[1, 4], [2, 5], [3, 6]]
reasoning: The transpose of a matrix is obtained by flipping rows and columns.
```

## Learn: Transpose of a Matrix

Consider a matrix \( M \) and its transpose \( M^T \):

Original Matrix \( M \):

$$
M = \begin{pmatrix} 
a & b & c \\ 
d & e & f 
\end{pmatrix}
$$

Transposed Matrix \( M^T \):

$$
M^T = \begin{pmatrix} 
a & d \\ 
b & e \\ 
c & f 
\end{pmatrix}
$$

Transposing a matrix involves converting its rows into columns and vice versa. This operation is fundamental in linear algebra for various computations and transformations.

## Solutions

### Custom Implementation

```python
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    l = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return l

a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(a=a))
```

### Alternative Custom Implementation

```python
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    matrix_a = list(zip(*a))
    return [list(row) for row in matrix_a]

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(a=a))
```

### NumPy Implementation

```python
import numpy as np

def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    return np.transpose(a)

a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(a=a))
```

## Code Explanation

### Custom Implementation

The first custom implementation of the `transpose_matrix` function uses nested list comprehensions to transpose the input matrix:

1. The outer list comprehension iterates over the columns of the input matrix by using the range of the number of columns (`range(len(a[0]))`).
2. The inner list comprehension iterates over the rows of the input matrix by using the range of the number of rows (`range(len(a))`).
3. For each column index `i`, a new row is created by extracting the element at index `i` from each row `j` of the input matrix.
4. The resulting transposed matrix is returned.

This implementation is efficient and directly converts rows to columns using list comprehensions.

### Alternative Custom Implementation

The second custom implementation uses the built-in `zip` function to transpose the matrix:

1. The `zip(*a)` expression unpacks the input matrix `a` and aggregates elements from each row into tuples representing the columns.
2. The `list(zip(*a))` converts these tuples into a list of tuples.
3. A list comprehension is used to convert each tuple (representing a row in the transposed matrix) into a list.
4. The resulting transposed matrix is returned.

This implementation is concise and leverages Python's built-in functions for readability and simplicity.

### NumPy Implementation

The NumPy implementation uses the `np.transpose` function to transpose the matrix:

1. The `np.transpose(a)` function is called with the input matrix `a`.
2. The function returns the transposed matrix as a NumPy array.

This implementation is highly efficient, especially for larger matrices, as it utilizes NumPy's optimized array operations. It is recommended when working with large datasets or when NumPy is already being used in the project.

By implementing these solutions, we can understand different approaches to transposing a matrix, each with its own advantages in terms of readability, simplicity, and performance.