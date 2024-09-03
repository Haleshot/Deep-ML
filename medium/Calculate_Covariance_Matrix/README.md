# Calculate Covariance Matrix (Medium) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Calculate Covariance Matrix](#learn-calculate-covariance-matrix)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Calculate Covariance Matrix](https://www.deep-ml.com/problem/Calculate%20Covariance%20Matrix)

Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

## Example

```python
input: vectors = [[1, 2, 3], [4, 5, 6]]
output: [[1.0, 1.0], [1.0, 1.0]]
reasoning: The dataset has two features with three observations each. The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.
```

## Learn: Calculate Covariance Matrix

The covariance matrix is a fundamental concept in statistics, illustrating how much two random variables change together. It's essential for understanding the relationships between variables in a dataset. For a dataset with $n$ features, the covariance matrix is an $n \times n$ square matrix where each element $(i, j)$ represents the covariance between the $i^{th}$ and $j^{th}$ features. Covariance is defined by the formula:

$$ \text{cov}(X, Y) = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{n-1} $$

Where:
- $X$ and $Y$ are two random variables (features),
- $x_i$ and $y_i$ are individual observations of $X$ and $Y$,
- $\bar{x}$ (x-bar) and $\bar{y}$ (y-bar) are the means of $X$ and $Y$,
- $n$ is the number of observations.

In the covariance matrix:
- The diagonal elements (where $i = j$) indicate the variance of each feature.
- The off-diagonal elements show the covariance between different features.

This matrix is symmetric, as the covariance between $X$ and $Y$ is equal to the covariance between $Y$ and $X$, denoted as $\text{cov}(X, Y) = \text{cov}(Y, X)$.

## Solutions

### Custom Implementation

```python
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    means = [sum(feature) / n_observations for feature in vectors]
    # print(covariance_matrix, "\n", means)

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n_observations)
            ) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix

# Example usage
vectors = [[1, 2, 3], [4, 5, 6]]
result = calculate_covariance_matrix(vectors)
print(result)
```

### NumPy Implementation

```python
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Convert the input list to a NumPy array for easier mathematical operations
    data = np.array(vectors)

    # Calculate the mean of each feature
    means = np.mean(data, axis=1)

    # Center the data by subtracting the mean of each feature
    centered_data = data - means[:, np.newaxis]

    # Number of observations (columns)
    n = data.shape[1]

    # Calculate the covariance matrix
    covariance_matrix = np.dot(centered_data, centered_data.T) / (n - 1)

    return covariance_matrix.tolist()

# Example usage
vectors = [[1, 2, 3], [4, 5, 6]]
result = calculate_covariance_matrix(vectors)
print(result)
```

## Code Explanation

### Custom Implementation

1. The function `calculate_covariance_matrix` takes a list of vectors as input.
2. It initializes variables for the number of features and observations, and creates an empty covariance matrix.
3. The means of each feature are calculated.
4. A commented print statement is included for debugging purposes, which would show the initial empty covariance matrix and the calculated means.
5. The function then iterates through each pair of features, calculating their covariance using the formula provided in the "Learn" section.
6. The covariance is stored symmetrically in the matrix (both at [i][j] and [j][i]).
7. Finally, the completed covariance matrix is returned.

This implementation follows the mathematical definition of covariance closely, making it easy to understand but potentially less efficient for large datasets.

### NumPy Implementation

1. The function first converts the input list to a NumPy array for efficient operations.
2. It calculates the mean of each feature using `np.mean()`.
3. The data is centered by subtracting the mean from each feature.
4. The number of observations is determined from the shape of the data.
5. The covariance matrix is calculated using matrix multiplication (`np.dot()`) of the centered data with its transpose, divided by (n-1).
6. The result is converted back to a list before being returned.

This implementation leverages NumPy's efficient array operations, making it faster for larger datasets. The use of matrix multiplication to calculate covariance is a common optimization in numerical libraries.

Both implementations produce the same result, but the NumPy version is likely to be more efficient, especially for larger datasets. The custom implementation, however, provides a clearer view of the step-by-step process of calculating the covariance matrix.
