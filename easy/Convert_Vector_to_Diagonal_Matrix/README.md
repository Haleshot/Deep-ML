# Convert Vector to Diagonal Matrix (Medium)

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Diagonal Matrices](#learn-understanding-diagonal-matrices)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Convert Vector to Diagonal Matrix](https://www.deep-ml.com/problem/Convert%20Vector%20to%20Diagonal%20Matrix)

Write a Python function to convert a 1D numpy array into a diagonal matrix. The function should take in a 1D numpy array `x` and return a 2D numpy array representing the diagonal matrix.

## Example

```python
x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)
# Output:
# [[1. 0. 0.]
#  [0. 2. 0.]
#  [0. 0. 3.]]
```

**Reasoning:** The input vector [1, 2, 3] is converted into a diagonal matrix where the elements of the vector form the diagonal of the matrix.

## Learn: Understanding Diagonal Matrices

A diagonal matrix is a square matrix in which the entries outside the main diagonal are all zero. The main diagonal is the set of entries extending from the top left to the bottom right of the matrix.

In this problem, you will write a function to convert a 1D numpy array (vector) into a diagonal matrix. The resulting matrix will have the elements of the input vector on its main diagonal, and zeros elsewhere.

Given a vector <img src="https://i.upmath.me/svg/%5Cmathbf%7Bx%7D%20%3D%20%5Bx_1%2C%20x_2%2C%20%5Cldots%2C%20x_n%5D" alt="\mathbf{x} = [x_1, x_2, \ldots, x_n]" />, the corresponding diagonal matrix <img src="https://i.upmath.me/svg/%5Cmathbf%7BD%7D" alt="\mathbf{D}" /> is:

<img src="https://i.upmath.me/svg/%0A%5Cmathbf%7BD%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%0Ax_1%20%26%200%20%26%200%20%26%20%5Ccdots%20%26%200%20%5C%5C%0A0%20%26%20x_2%20%26%200%20%26%20%5Ccdots%20%26%200%20%5C%5C%0A0%20%26%200%20%26%20x_3%20%26%20%5Ccdots%20%26%200%20%5C%5C%0A%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%5C%5C%0A0%20%26%200%20%26%200%20%26%20%5Ccdots%20%26%20x_n%0A%5Cend%7Bbmatrix%7D%0A" alt="
\mathbf{D} = \begin{bmatrix}
x_1 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; x_2 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; 0 &amp; x_3 &amp; \cdots &amp; 0 \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; x_n
\end{bmatrix}
" />

Diagonal matrices are important in various mathematical and scientific computations because of their simple structure and properties.

## Solutions

### Custom Implementation

```python
import numpy as np

def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
    l = [[0] * len(x) for _ in range(len(x))]
    for i in range(len(x)):
        l[i][i] = x[i]
    return np.array(l).tolist()

x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)
```

### NumPy Implementation

```python
import numpy as np

def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
    return np.identity(np.size(x)) * x

x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)
```

## Code Explanation

The custom implementation of the `make_diagonal` function takes a 1D numpy array `x` as input and returns a 2D list representing the diagonal matrix. Here's how it works:

1. It initializes a 2D list `l` with dimensions `len(x) x len(x)`, filled with zeros.
2. It then iterates through the range of `len(x)`.
3. For each index `i`, it sets the element at position `[i][i]` (the diagonal) to the corresponding value from the input array `x`.
4. Finally, it converts the 2D list to a numpy array and then back to a list using `np.array(l).tolist()`.

This implementation directly applies the definition of a diagonal matrix by creating a square matrix with zeros and placing the input vector elements along the main diagonal.

The NumPy implementation, on the other hand, utilizes NumPy's built-in functions for a more concise solution. It uses `np.identity()` to create an identity matrix of the same size as the input vector, and then multiplies it element-wise with the input vector using the `*` operator.

Both implementations produce the same result, but the NumPy version is more efficient, especially for larger inputs, as it leverages NumPy's optimized array operations.