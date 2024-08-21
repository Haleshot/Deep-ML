# Ridge Regression Loss Function (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Ridge Regression Loss](#learn-ridge-regression-loss)
  - [Key Concepts](#key-concepts)
  - [Ridge Loss Function](#ridge-loss-function)
  - [Implementation Steps](#implementation-steps)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Implement Ridge Regression Loss Function](https://www.deep-ml.com/problem/Ridge%20Regression%20Loss)

Write a Python function `ridge_loss` that implements the Ridge Regression loss function. The function should take a 2D numpy array `X` representing the feature matrix, a 1D numpy array `w` representing the coefficients, a 1D numpy array `y_true` representing the true labels, and a float `alpha` representing the regularization parameter. The function should return the Ridge loss, which combines the Mean Squared Error (MSE) and a regularization term.

## Example

```python
import numpy as np

X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)
# Expected Output: 2.204
```

## Learn: Ridge Regression Loss

Ridge Regression is a linear regression method with a regularization term to prevent overfitting by controlling the size of the coefficients.

### Key Concepts

1. **Regularization**: Adds a penalty to the loss function to discourage large coefficients, helping to generalize the model.
2. **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
3. **Penalty Term**: The sum of the squared coefficients, scaled by the regularization parameter α, which controls the strength of the regularization.

### Ridge Loss Function

The Ridge Loss function combines MSE and the penalty term:


```math
L(\beta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \alpha \sum_{j=1}^{p} \beta_j^2
```

Where:
- $n$ is the number of samples
- $y_i$ is the true value for the $i$-th sample
- $\hat{y}_i$ is the predicted value for the $i$-th sample
- $\lambda$ is the regularization parameter (alpha)
- $\beta_j$ are the coefficients (w)
- $p$ is the number of features

### Implementation Steps

1. **Calculate MSE**: Compute the average squared difference between actual and predicted values.
2. **Add Regularization Term**: Compute the sum of squared coefficients multiplied by α.
3. **Combine and Minimize**: Sum MSE and the regularization term to form the Ridge loss, then minimize this loss to find the optimal coefficients.

## Solutions

### Custom Implementation

```python
import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    y_pred = []
    for i in range(len(X)):
        temp = 0
        for j in range(len(w)):
            temp += X[i][j] * w[j]
        y_pred.append(temp)

    MSE = sum((((y_true - y_pred) ** 2) / len(X)).tolist())
    sum_w = sum([i**2 for i in w])
    reg = alpha * sum_w
    return MSE + reg
```

### NumPy Implementation

```python
import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    y_pred = (X @ w).tolist()
    MSE = np.mean((y_true - y_pred)**2).tolist()
    reg = alpha * np.sum(w**2).tolist()
    return MSE + reg
```

## Code Explanation

Both implementations of the `ridge_loss` function take four parameters:
- `X`: a 2D numpy array representing the feature matrix
- `w`: a 1D numpy array representing the coefficients
- `y_true`: a 1D numpy array representing the true labels
- `alpha`: a float representing the regularization parameter

The functions work as follows:

1. **Custom Implementation**:
   - Calculates the predicted values `y_pred` using a nested loop to perform matrix multiplication.
   - Computes the Mean Squared Error (MSE) by summing the squared differences between true and predicted values, divided by the number of samples.
   - Calculates the sum of squared coefficients `sum_w`.
   - Computes the regularization term `reg` by multiplying `alpha` with `sum_w`.
   - Returns the sum of MSE and the regularization term.

2. **NumPy Implementation**:
   - Uses NumPy's matrix multiplication `@` to calculate the predicted values `y_pred`.
   - Computes the MSE using NumPy's `mean` function.
   - Calculates the regularization term using NumPy's `sum` function on the squared coefficients.
   - Returns the sum of MSE and the regularization term.

Both implementations produce the same result, but the NumPy version is more concise and potentially more efficient, especially for larger matrices, as it leverages NumPy's optimized array operations.

The custom implementation provides a more explicit calculation process, which can be helpful for understanding the steps involved in computing the Ridge Regression loss. However, for performance and simplicity, the NumPy implementation is generally preferred in practical applications.
