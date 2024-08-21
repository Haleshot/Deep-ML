# ReLU Activation Function (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding the ReLU Activation Function](#learn-understanding-the-relu-activation-function)
  - [Mathematical Definition](#mathematical-definition)
  - [Characteristics](#characteristics)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[ReLU Activation Function](https://www.deep-ml.com/problem/ReLU%20Activation%20Function)

Write a Python function `relu` that implements the Rectified Linear Unit (ReLU) activation function. The function should take a single float as input and return the value after applying the ReLU function. The ReLU function returns the input if it's greater than 0, otherwise, it returns 0.

## Example

```python
print(relu(0)) 
# Output: 0

print(relu(1)) 
# Output: 1

print(relu(-1)) 
# Output: 0
```

## Learn: Understanding the ReLU Activation Function

The ReLU (Rectified Linear Unit) activation function is widely used in neural networks, particularly in hidden layers of deep learning models. It maps any real-valued number to the non-negative range $$[0, \infty)$$, which helps introduce non-linearity into the model while maintaining computational efficiency.

### Mathematical Definition

The ReLU function is mathematically defined as:

$$f(z) = \max(0, z)$$

Where $z$ is the input to the function.

### Characteristics

1. **Output Range**: The output is always in the range $$[0, \infty)$$. Values below 0 are mapped to 0, while positive values are retained.

2. **Shape**: The function has an "L" shaped curve with a horizontal axis at $z = 0$ and a linear increase for positive $z$.

3. **Gradient**: The gradient is 1 for positive values of $z$ and 0 for non-positive values. This means the function is linear for positive inputs and flat (zero gradient) for negative inputs.

This function is particularly useful in deep learning models as it introduces non-linearity while being computationally efficient, helping to capture complex patterns in the data.

## Solutions

### Custom Implementation

```python
import math

def relu(z: float) -> float:
    return max(0, z)

# Testing
print(relu(2))
```

### NumPy Implementation

```python
import numpy as np

def relu(z: float) -> float:
    return np.maximum(0, z)

# Testing
print(relu(2))
```

## Code Explanation

The problem has been solved using two different approaches: a custom built-in method and using NumPy's built-in function.

1. **Custom Implementation**:
   The custom implementation uses Python's built-in `max()` function to compare 0 and the input `z`. This elegantly captures the ReLU function's behavior: returning 0 for negative inputs and the input itself for positive values.

2. **NumPy Implementation**:
   The NumPy implementation uses the `np.maximum()` function, which performs element-wise maximum comparison between two arrays or values. In this case, it compares 0 and the input `z`, effectively implementing the ReLU function.

Both implementations achieve the same result, but the NumPy version might be more efficient for large-scale operations or when working with arrays of data. The custom implementation is straightforward and doesn't require additional libraries, making it suitable for simpler applications or when NumPy is not available.

The `relu()` function is typed with Python's type hints, indicating that it takes a float as input and returns a float. This enhances code readability and can help catch type-related errors early in development.
