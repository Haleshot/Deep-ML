# Implementation of Log Softmax Function (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Log Softmax Function](#learn-understanding-log-softmax-function)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Implementation of Log Softmax Function](https://www.deep-ml.com/problem/Log%20Softmax)

In machine learning and statistics, the softmax function is a generalization of the logistic function that converts a vector of scores into probabilities. The log-softmax function is the logarithm of the softmax function, and it is often used for numerical stability when computing the softmax of large numbers. Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.

## Example

```python
A = np.array([1, 2, 3])
print(log_softmax(A))

Output:
array([-2.4076, -1.4076, -0.4076])
```

## Learn: Understanding Log Softmax Function

The log softmax function is a numerically stable way of calculating the logarithm of the softmax function. The softmax function converts a vector of arbitrary values (logits) into a vector of probabilities, where each value lies between 0 and 1, and the values sum to 1. The softmax function is given by:

$$\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}}$$

However, directly applying the logarithm to the softmax function can lead to numerical instability, especially when dealing with large numbers. To prevent this, we use the log-softmax function, which incorporates a shift by subtracting the maximum value from the input vector:

$$
\text{log-softmax}(x_i) = x_i - \max(x) - \log\left(\sum_{j=1}^n e^{x_j - \max(x)}\right)
$$

This formulation helps to avoid overflow issues that can occur when exponentiating large numbers. The log-softmax function is particularly useful in machine learning for calculating probabilities in a stable manner, especially when used with cross-entropy loss functions.

## Solutions

### Custom Implementation

```python
import numpy as np

def log_softmax(scores: list[int | float]) -> np.ndarray:
    total_log = np.sum([np.exp(i - max(scores)) for i in scores])
    log_softmax = [scores[i] - max(scores) - np.log(total_log) for i in range(len(scores))]
    return log_softmax # type: ignore

A = np.array([1, 2, 3])
print(log_softmax(A))
```

### NumPy Implementation

```python
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # Subtract the maximum value for numerical stability
    scores = scores - np.max(scores)
    return scores - np.log(np.sum(np.exp(scores)))

A = np.array([1, 2, 3])
print(log_softmax(A))
```

## Code Explanation

Two implementations of the log_softmax function are provided: a custom implementation and a NumPy-based implementation.

### Custom Implementation

The custom implementation follows these steps:

1. Calculate the maximum value of the input scores.
2. Compute the exponential of each score minus the maximum value.
3. Sum these exponentials to get the total_log.
4. Calculate the log-softmax for each score using the formula:
   log_softmax(x_i) = x_i - max(x) - log(total_log)
5. Return the resulting list of log-softmax values.

This implementation closely follows the mathematical definition of the log-softmax function, providing a clear and intuitive approach.

### NumPy Implementation

The NumPy implementation leverages built-in NumPy functions for efficient computation:

1. Subtract the maximum value from all scores for numerical stability.
2. Apply the exponential function to all shifted scores.
3. Sum the exponentials and take the logarithm.
4. Subtract this logarithm from the shifted scores.

This implementation is more concise and potentially more efficient, especially for larger input arrays, as it utilizes NumPy's vectorized operations.

Both implementations produce the same result but differ in their approach. The custom implementation provides a more explicit calculation process, while the NumPy version is more compact and may offer better performance for larger datasets.
