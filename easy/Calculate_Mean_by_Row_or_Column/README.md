# Calculate Mean by Row or Column (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Calculate Mean by Row or Column](#learn-calculate-mean-by-row-or-column)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [Alternative Custom Implementation](#alternative-custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Calculate Mean by Row or Column](https://www.deep-ml.com/problem/Calculate%20Mean%20by%20Row%20or%20Column)

Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

## Example

```python
# Example 1:
input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
output: [4.0, 5.0, 6.0]
reasoning: Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].

# Example 2:
input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'row'
output: [2.0, 5.0, 8.0]
reasoning: Calculating the mean of each row results in [(1+2+3)/3, (4+5+6)/3, (7+8+9)/3].
```

## Learn: Calculate Mean by Row or Column

Calculating the mean of a matrix by row or column involves averaging the elements across the specified dimension. This operation provides insights into the distribution of values within the dataset, useful for data normalization and scaling.

### Row Mean

The mean of a row is computed by summing all elements in the row and dividing by the number of elements. For row \(i\), the mean is:

$$
\mu_{\text{row } i} = \frac{1}{n} \sum_{j=1}^{n} a_{ij}
$$

where \(a_{ij}\) is the matrix element in the \(i^{th}\) row and \(j^{th}\) column, and \(n\) is the total number of columns.

### Column Mean

Similarly, the mean of a column is found by summing all elements in the column and dividing by the number of elements. For column \(j\), the mean is:

$$
\mu_{\text{column } j} = \frac{1}{m} \sum_{i=1}^{m} a_{ij}
$$

where \(m\) is the total number of rows.

This mathematical formulation helps in understanding how data is aggregated across different dimensions, a critical step in various data preprocessing techniques.

## Solutions

### Custom Implementation

```python
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    l = []
    if mode == "row":
        for n in range(len(matrix)):
            sum = 0
            for i in matrix[n]:
                sum += i
            l.append(sum/len(matrix))

    elif mode == "column":
        for i in range(0, len(matrix)):
            sum = 0
            for j in range(0, len(matrix)):
                sum += matrix[j][i]
            l.append(sum/len(matrix[0]))
     
    return l

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix=matrix, mode=mode))
```

### Alternative Custom Implementation

```python
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        return [sum(row) / len(row) for row in matrix]
    elif mode == "column":
        return [sum(col) / len(matrix) for col in zip(*matrix)]
    else:
        raise ValueError("Mode must be of type 'row' or 'column' ")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix=matrix, mode=mode))
```

### NumPy Implementation

```python
import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        return np.array(np.sum(matrix, axis=0) // len(matrix)).tolist()
    elif mode == "column":
        return np.array(np.sum(matrix, axis=1) // len(matrix[0])).tolist()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix=matrix, mode=mode))
```

## Code Explanation

The custom implementation of `calculate_matrix_mean` function takes two parameters:

- `matrix`: a 2D list representing the input matrix
- `mode`: a string that specifies whether to calculate the mean by 'row' or by 'column'

The function works as follows:

1. It initializes an empty list `l` to store the result.
2. If the mode is 'row':
   - It iterates through each row `n` of the matrix.
   - For each row, it calculates the sum of the elements and then divides by the number of elements to get the mean.
   - The mean is appended to the list `l`.
3. If the mode is 'column':
   - It iterates through each column index `i`.
   - For each column, it calculates the sum of the elements by iterating through each row and then divides by the number of elements to get the mean.
   - The mean is appended to the list `l`.
4. Finally, it returns the list `l` containing the means.

The alternative custom implementation simplifies the logic using list comprehensions and the built-in `zip` function to transpose the matrix for column-wise operations.

The NumPy implementation leverages NumPy's optimized array operations for potentially more efficient calculations, especially useful for larger matrices.
