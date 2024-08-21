# Transformation Matrix from Basis B to C (Difficult) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Transformation Matrices](#learn-understanding-transformation-matrices)
- [Solution](#solution)
- [Code Explanation](#code-explanation)
- [Resources](#resources)

## Problem Statement

[Transformation Matrix from Basis B to C](https://www.deep-ml.com/problem/Transformation%20Matrix%20from%20Basis%20B%20to%20C)

Given basis vectors in two different bases B and C for R^3, write a Python function to compute the transformation matrix P from basis B to C.

## Example

```python
B = [[1, 0, 0], 
     [0, 1, 0], 
     [0, 0, 1]]
C = [[1, 2.3, 3], 
     [4.4, 25, 6], 
     [7.4, 8, 9]]
output: [[-0.6772, -0.0126, 0.2342],
        [-0.0184, 0.0505, -0.0275],
        [0.5732, -0.0345, -0.0569]]
```

Reasoning: The transformation matrix P from basis B to C can be found using matrix operations involving the inverse of matrix C.

## Learn: Understanding Transformation Matrices

A transformation matrix allows us to convert the coordinates of a vector in one basis to coordinates in another basis. For bases B and C of a vector space, the transformation matrix P from B to C is calculated by:

1. Inverse of Basis C: First, find the inverse of the matrix representing basis C, denoted $$C^{-1}$$.

2. Matrix Multiplication: Multiply $$C^{-1}$$ by the matrix of basis B. The result is the transformation matrix P, where:

   $$P = C^{-1} * B$$

This matrix P can be used to transform any vector coordinates from the B basis to the C basis.

## Solution

```python
import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    return np.dot(np.linalg.inv(C), B)  # type: ignore

B = [[1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1]]

C = [[1, 2.3, 3], 
    [4.4, 25, 6], 
    [7.4, 8, 9]]

print(transform_basis(B=B, C=C))
```

## Code Explanation

The `transform_basis` function implements the transformation matrix calculation using NumPy's built-in methods. Here's a breakdown of the implementation:

1. The function takes two parameters:
   - `B`: A list of lists representing the basis vectors in the B coordinate system.
   - `C`: A list of lists representing the basis vectors in the C coordinate system.

2. `np.linalg.inv(C)`: This NumPy function calculates the inverse of matrix C.

3. `np.dot(np.linalg.inv(C), B)`: The `np.dot` function performs matrix multiplication between the inverse of C and B, resulting in the transformation matrix P.

4. The function returns the resulting transformation matrix.

This implementation leverages NumPy's efficient matrix operations, making it suitable for larger matrices and providing high numerical precision.

## Resources

- [Change of basis | Chapter 13, Essence of linear algebra](https://youtu.be/P2LTAUO1TdA?si=O8XAmMrfpZizOr81) by 3Blue1Brown

This video provides an excellent visual explanation of the change of basis concept, which is fundamental to understanding transformation matrices.
