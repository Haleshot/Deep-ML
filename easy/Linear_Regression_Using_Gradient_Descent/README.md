# Linear Regression Using Gradient Descent (easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Linear Regression Using Gradient Descent](#learn-linear-regression-using-gradient-descent)
- [Solutions](#solutions)
  - [Implementation 1: Detailed Approach](#implementation-1-detailed-approach)
  - [Implementation 2: Compact Approach](#implementation-2-compact-approach)
- [Code Explanation](#code-explanation)

## Problem Statement

[Linear Regression Using Gradient Descent](https://www.deep-ml.com/problem/Linear%20Regression%20Using%20Gradient%20Descent)

Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

## Example

```python
input: X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000
output: np.array([0.1107, 0.9513])
reasoning: The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.
```

## Learn: Linear Regression Using Gradient Descent

Linear regression can be performed using gradient descent, where the coefficients (or weights) of the model are iteratively adjusted to minimize a cost function (usually mean squared error). This method is particularly useful when the number of features is large or when the feature matrix is not invertible.

The gradient descent algorithm updates the weights by moving in the direction of the negative gradient of the cost function with respect to the weights. The update rule for each weight is given by:

$$\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})x_j^{(i)}$$

Where:
- $\alpha$ is the learning rate
- $m$ is the number of training examples
- $h_{\theta}(x^{(i)})$ is the hypothesis function at iteration $i$
- $x^{(i)}$ is the feature vector of the $i^{th}$ training example
- $y^{(i)}$ is the actual target value for the $i^{th}$ training example
- $x_j^{(i)}$ is the value of feature $j$ for the $i^{th}$ training example

**Note**: The choice of learning rate and the number of iterations are crucial for the convergence and performance of gradient descent. Too small a learning rate may lead to slow convergence, while too large a learning rate may cause overshooting and divergence.

## Solutions

### Implementation 1: Detailed Approach

```python
import numpy as np

def linear_regression_gradient_descent(X, y, alpha, num_iterations) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Parameters:
    X : numpy.ndarray
        Feature matrix including a column of ones for the intercept.
    y : numpy.ndarray
        Target vector.
    alpha : float
        Learning rate.
    num_iterations : int
        Number of iterations for gradient descent.

    Returns:
    numpy.ndarray
        Coefficients of the linear regression model rounded to four decimal places.
    """
    # Number of training examples
    m = len(y)

    # Initialize weights (coefficients) to zeros
    theta = np.zeros(X.shape[1])

    for i in range(num_iterations):
        # Compute predictions
        predictions = X.dot(theta)

        # Compute the error (difference between predictions and actual values)
        errors = predictions - y

        # Compute the gradient of the cost function with respect to each weight
        gradient = (1 / m) * X.T.dot(errors)

        # Update the weights by moving in the opposite direction of the gradient
        theta -= alpha * gradient

    # Round the coefficients to four decimal places
    theta = np.round(theta, 4)

    return theta
```

### Implementation 2: Compact Approach

```python
import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        predictions = X @ theta
        errors = predictions - y.reshape(-1, 1)
        updates = X.T @ errors / m
        theta -= alpha * updates
    return np.round(theta.flatten(), 4)
```

## Code Explanation

Both implementations perform linear regression using gradient descent, but they differ in their approach and level of detail.

### Implementation 1: Detailed Approach

This implementation provides a more verbose and step-by-step approach:

1. It initializes the weights (theta) as a 1D array of zeros.
2. In each iteration:
   - It computes predictions using the dot product of X and theta.
   - It calculates the errors by subtracting the actual values from the predictions.
   - It computes the gradient using the formula derived from the cost function.
   - It updates the weights using the gradient descent update rule.
3. Finally, it rounds the coefficients to four decimal places.

This implementation is more explicit and easier to understand for those new to gradient descent.

### Implementation 2: Compact Approach

This implementation takes a more concise approach:

1. It initializes theta as a 2D column vector of zeros.
2. In each iteration:
   - It computes predictions using matrix multiplication (X @ theta).
   - It calculates errors, reshaping y to ensure correct dimensions.
   - It computes updates in a single line, combining gradient calculation and scaling.
   - It updates theta using the computed updates.
3. It returns the flattened and rounded theta.

This implementation is more compact and uses NumPy's broadcasting capabilities for efficient computation.

Both implementations will produce similar results, but the second one may be slightly more efficient due to its use of matrix operations. The choice between them depends on the need for readability versus compactness in the codebase.
