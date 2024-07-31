# Matrix times Vector (Easy)

## Problem Statement

Write a Python function that takes the dot product of a matrix and a vector. Return -1 if the matrix could not be dotted with the vector.

### Example:

```python
input: a = [[1,2],[2,4]], b = [1,2]
output: [5, 10]
reasoning: 1*1 + 2*2 = 5
           1*2 + 2*4 = 10
```

## Matrix Times Vector

Consider a matrix $A$ and a vector $v$, where:

Matrix $A$:

$$
A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}
$$

Vector $v$:

$$
v = \begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}
$$

The dot product of $A$ and $v$ results in a new vector:

$$
A \cdot v = \begin{pmatrix}
a_{11}v_1 + a_{12}v_2 \\
a_{21}v_1 + a_{22}v_2
\end{pmatrix}
$$

### Things to note:
An $m \times n$ matrix will need to be multiplied by a vector of size $n$ or else this will not work.

### Code explanation:
The function `matrix_dot_vector` takes two parameters:
- `a`: a 2D list representing the matrix
- `b`: a 1D list representing the vector

The function attempts to compute the dot product of the matrix and vector. However, there's a small error in the condition. It should check if the number of columns in the matrix (len(a[0])) is equal to the length of the vector (len(b)), not if the number of rows in the matrix (len(a)) is equal to the length of the vector.

If the dimensions are compatible, it computes the dot product:
1. It iterates through each row of the matrix.
2. For each row, it computes the sum of element-wise products with the vector.
3. The result is appended to a list `l`.
4. Finally, it returns the list `l` containing the dot product results.

If the dimensions are not compatible, it returns -1.
