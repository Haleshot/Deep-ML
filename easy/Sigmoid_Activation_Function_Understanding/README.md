# Sigmoid Activation Function Understanding (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding the Sigmoid Activation Function](#learn-understanding-the-sigmoid-activation-function)
  - [Mathematical Definition](#mathematical-definition)
  - [Characteristics](#characteristics)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Sigmoid Activation Function Understanding](https://www.deep-ml.com/problem/Sigmoid%20Activation%20Function%20Understanding)

Write a Python function that computes the output of the sigmoid activation function given an input value z. The function should return the output rounded to four decimal places.

## Example

```python
input: z = 0
output: 0.5
reasoning: The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)). For z = 0, exp(-0) = 1, hence the output is 1 / (1 + 1) = 0.5.
```

## Learn: Understanding the Sigmoid Activation Function

The sigmoid activation function is crucial in neural networks, especially for binary classification tasks. It maps any real-valued number into the (0, 1) interval, making it useful for modeling probability as an output.

### Mathematical Definition

The sigmoid function is mathematically defined as:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where $z$ is the input to the function.

### Characteristics

- **Output Range**: The output is always between 0 and 1.
- **Shape**: It has an "S" shaped curve.
- **Gradient**: The function's gradient is highest near $z = 0$ and decreases toward either end of the z-axis.

This function is particularly useful for turning logits (raw prediction values) into probabilities in binary classification models.

## Solutions

### Custom Implementation

```python
import math

def sigmoid(z):
    return round(1 / (1 + math.exp(-z)), 4)

# Test the function
print(sigmoid(0))  # Should output 0.5
```

### NumPy Implementation

```python
import numpy as np

def sigmoid(z):
    return round(1 / (1 + np.exp(-z)), 4)

# Test the function
print(sigmoid(0))  # Should output 0.5
```

## Code Explanation

Both implementations of the `sigmoid` function take a single parameter `z`, which is the input to the sigmoid function. The function calculates the sigmoid value and rounds it to four decimal places as required.

1. **Custom Implementation**:
   - This version uses Python's built-in `math` module.
   - It directly implements the sigmoid formula: $\frac{1}{1 + e^{-z}}$.
   - The `math.exp()` function is used to calculate $e^{-z}$.

2. **NumPy Implementation**:
   - This version uses the NumPy library, which is commonly used for numerical computations in Python.
   - The implementation is very similar to the custom one, but it uses `np.exp()` instead of `math.exp()`.
   - NumPy's implementation can be more efficient, especially when dealing with arrays of inputs.

Both implementations use the `round()` function to limit the output to four decimal places.

The main difference between these implementations is the library used for the exponential function. The NumPy version might be preferred in scenarios where you're already using NumPy in your project or when you need to apply the sigmoid function to arrays of values efficiently.

These implementations provide a straightforward and efficient way to calculate the sigmoid function, which is essential in many machine learning algorithms, particularly in neural networks for binary classification tasks.
