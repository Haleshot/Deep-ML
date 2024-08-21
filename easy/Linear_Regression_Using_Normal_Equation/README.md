# Linear Regression Using Normal Equation (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Linear Regression Using the Normal Equation](#learn-linear-regression-using-the-normal-equation)
- [Solutions](#solutions)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Linear Regression Using Normal Equation](https://www.deep-ml.com/problem/Linear%20Regression%20Using%20Normal%20Equation)

Write a Python function that performs linear regression using the normal equation. The function should take a matrix X (features) and a vector y (target) as input, and return the coefficients of the linear regression model. Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

## Example

```python
input: X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]
output: [0.0, 1.0]
reasoning: The linear model is y = 0.0 + 1.0*x, perfectly fitting the input data.
```

## Learn: Linear Regression Using the Normal Equation

Linear regression aims to model the relationship between a scalar dependent variable $$y$$ and one or more explanatory variables (or independent variables) $$X$$. The normal equation provides an analytical solution to finding the coefficients $$\theta$$ that minimize the cost function for linear regression.

Given a matrix $$X$$ (with each row representing a training example and each column a feature) and a vector $$y$$ (representing the target values), the normal equation is:

$$\theta = (X^TX)^{-1}X^Ty$$

Where:
- $$X^T$$ is the transpose of $$X$$,
- $$(X^TX)^{-1}$$ is the inverse of the matrix $$X^TX$$,
- $$y$$ is the vector of target values.

**Things to note**: This method does not require any feature scaling, and there's no need to choose a learning rate. However, computing the inverse of $$X^TX$$ can be computationally expensive if the number of features is very large.

### Practical Implementation

A practical implementation involves augmenting $$X$$ with a column of ones to account for the intercept term and then applying the normal equation directly to compute $$\theta$$.

## Solutions

### NumPy Implementation (Step 1)

```python
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    mat = np.dot(np.transpose(X), X)
    mat = np.linalg.inv(mat)
    mult = np.dot(np.transpose(X), y)
    theta = np.dot(mat, mult)
    return np.round(theta, 2)

X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X=X, y=y))
```

### NumPy Implementation (Step 2)

```python
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    X_transpose = X.T
    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    theta = np.round(theta, 4).flatten().tolist()
    return theta

X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X=X, y=y))
```

## Code Explanation

Both implementations use NumPy's built-in methods to solve the normal equation for linear regression, but they differ slightly in their approach:

### Step 1 Implementation:

1. `np.dot(np.transpose(X), X)`: Calculates $$X^TX$$.
2. `np.linalg.inv(mat)`: Computes $$(X^TX)^{-1}$$.
3. `np.dot(np.transpose(X), y)`: Calculates $$X^Ty$$.
4. `np.dot(mat, mult)`: Performs the final multiplication to get $$\theta = (X^TX)^{-1}X^Ty$$.
5. `np.round(theta, 2)`: Rounds the result to two decimal places.

This implementation directly applies the normal equation using separate steps for each matrix operation.

### Step 2 Implementation:

1. `X = np.array(X)` and `y = np.array(y).reshape(-1, 1)`: Converts input lists to NumPy arrays, reshaping y to a column vector.
2. `X_transpose = X.T`: Computes the transpose of X.
3. `np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)`: Applies the entire normal equation $$(X^TX)^{-1}X^Ty$$ in one line.
4. `np.round(theta, 4).flatten().tolist()`: Rounds to four decimal places, flattens the result, and converts back to a list.

This implementation is more concise, combining multiple steps into a single line for the core calculation.

Both implementations effectively solve the normal equation, with the main differences being:
1. The precision of rounding (2 vs 4 decimal places)
2. The return type (NumPy array vs Python list)
3. The structure of the calculation (separate steps vs combined operation)

The choice between these implementations might depend on specific requirements for precision, output format, and personal preference for code structure.
