# Reshape Matrix (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Reshaping a Matrix](#learn-reshaping-a-matrix)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Reshape Matrix](https://www.deep-ml.com/problem/Reshape%20Matrix)

Write a Python function that reshapes a given matrix into a specified shape.

## Example

```python
input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
output: [[1, 2], [3, 4], [5, 6], [7, 8]]
reasoning: The given matrix is reshaped from 2x4 to 4x2.
```

## Learn: Reshaping a Matrix

Matrix reshaping involves changing the shape of a matrix without altering its data. This is essential in many machine learning tasks where the input data needs to be formatted in a specific way. For example, consider a matrix $M$:

Original Matrix $M$:

$$
M = \begin{pmatrix} 
1 & 2 & 3 & 4 \\ 
5 & 6 & 7 & 8 
\end{pmatrix}
$$

Reshaped Matrix $M'$ with shape (4, 2):

$$
M' = \begin{pmatrix} 
1 & 2 \\ 
3 & 4 \\ 
5 & 6 \\ 
7 & 8 
\end{pmatrix}
$$

Ensure the total number of elements remains constant during reshaping.

## Solutions

### Custom Implementation

```python
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    l = [[0] * new_shape[1] for _ in range(new_shape[0])]
    flat_a = [elem for row in a for elem in row]  # Flatten the original matrix
    # print(flat_a)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            l[i][j] = flat_a[i * new_shape[1] + j] # type: ignore
    return l # type: ignore

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
print(reshape_matrix(a=a, new_shape=new_shape)) # type: ignore
```

### NumPy Implementation

```python
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
    return np.reshape(a, newshape=new_shape).tolist()

# Usage remains the same as the custom implementation
```

## Code Explanation

The custom implementation of `reshape_matrix` function takes two parameters:

- `a`: a 2D list representing the input matrix
- `new_shape`: a tuple of two integers specifying the desired shape of the output matrix

The function works as follows:

1. It initializes a new 2D list `l` with the desired shape, filled with zeros.
2. It flattens the input matrix `a` into a 1D list `flat_a` using a list comprehension.
3. It then iterates through the new matrix shape, filling it with elements from the flattened input matrix.
4. The index calculation `i * new_shape[1] + j` ensures that elements are placed in the correct position in the reshaped matrix.
5. Finally, it returns the reshaped matrix `l`.

This implementation manually handles the reshaping process, providing a clear understanding of how matrix reshaping works at a fundamental level.

The NumPy implementation, on the other hand, utilizes the built-in `np.reshape()` function from the NumPy library. This method is more concise and potentially more efficient, especially for larger matrices, as it leverages NumPy's optimized array operations. The `tolist()` method is then used to convert the NumPy array back to a Python list, ensuring compatibility with the function's return type.

Both implementations will produce the same result, but the NumPy version may be preferred in scenarios where performance is critical or when working with larger datasets that are already in NumPy array format.
