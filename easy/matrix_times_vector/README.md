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