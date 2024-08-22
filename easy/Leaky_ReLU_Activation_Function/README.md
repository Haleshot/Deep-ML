# Leaky ReLU Activation Function (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding the Leaky ReLU Activation Function](#learn-understanding-the-leaky-relu-activation-function)
  - [Mathematical Definition](#mathematical-definition)
  - [Characteristics](#characteristics)
- [Solution](#solution)
  - [Custom Implementation](#custom-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Leaky ReLU Activation Function](https://www.deep-ml.com/problem/Leaky%20ReLU)

Write a Python function `leaky_relu` that implements the Leaky Rectified Linear Unit (Leaky ReLU) activation function. The function should take a float `z` as input and an optional float `alpha`, with a default value of 0.01, as the slope for negative inputs. The function should return the value after applying the Leaky ReLU function.

## Example

```python
print(leaky_relu(0)) 
# Output: 0

print(leaky_relu(1)) 
# Output: 1

print(leaky_relu(-1)) 
# Output: -0.01

print(leaky_relu(-2, alpha=0.1))
# Output: -0.2
```

## Learn: Understanding the Leaky ReLU Activation Function

The Leaky ReLU (Leaky Rectified Linear Unit) activation function is a variant of the ReLU function used in neural networks. It addresses the "dying ReLU" problem by allowing a small, non-zero gradient when the input is negative. This small slope for negative inputs helps keep the function active and helps prevent neurons from becoming inactive.

### Mathematical Definition

The Leaky ReLU function is mathematically defined as:

$$
f(z) = \begin{cases} 
z & \text{if } z > 0 \\
\alpha z & \text{if } z \leq 0 
\end{cases}
$$

Where $z$ is the input to the function and $\alpha$ is a small positive constant, typically $0.01$.

In this definition, the function returns $z$ for positive values, and for negative values, it returns $\alpha z$, allowing a small gradient to pass through.

### Characteristics

- **Output Range**: The output is in the range $(-\infty, \infty)$. Positive values are retained, while negative values are scaled by the factor $\alpha$, allowing them to be slightly negative.
- **Shape**: The function has a similar "L" shaped curve as ReLU, but with a small negative slope on the left side for negative $z$, creating a small gradient for negative inputs.
- **Gradient**: The gradient is 1 for positive values of $z$ and $\alpha$ for non-positive values. This allows the function to remain active even for negative inputs, unlike ReLU, where the gradient is zero for negative inputs.

This function is particularly useful in deep learning models as it mitigates the issue of "dead neurons" in ReLU by ensuring that neurons can still propagate a gradient even when the input is negative, helping to improve learning dynamics in the network.

## Solution

### Custom Implementation

```python
import numpy as np
import math

def leaky_relu(z: float, alpha: float = 0.01) -> float | int: # type: ignore
    # Your code here
    if z > 0:
        return z
    else:
        return alpha * z

print(leaky_relu(0))
# Output: 0

print(leaky_relu(1))
# Output: 1

print(leaky_relu(-1))
# Output: -0.01

print(leaky_relu(-2, alpha=0.1))
# Output: -0.2

```

## Code Explanation

The custom implementation of the `leaky_relu` function takes two parameters:

- `z`: a float value representing the input to the function
- `alpha`: an optional float value (default 0.01) representing the slope for negative inputs

The function works as follows:

1. It checks if the input `z` is greater than 0.
2. If `z` is positive, it returns `z` unchanged.
3. If `z` is non-positive (zero or negative), it returns `alpha * z`.

This implementation directly applies the mathematical definition of the Leaky ReLU function. It preserves positive inputs and scales negative inputs by the factor `alpha`, allowing a small gradient to pass through for negative values.

Note: The `# type: ignore` comment is used to suppress type checking warnings, as the function's return type annotation includes both `float` and `int`.
