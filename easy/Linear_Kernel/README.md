# Linear Kernel Function (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding the Linear Kernel](#learn-understanding-the-linear-kernel)
  - [Mathematical Definition](#mathematical-definition)
  - [Characteristics](#characteristics)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementations](#numpy-implementations)
- [Code Explanation](#code-explanation)
- [Note on Multidimensional Arrays](#note-on-multidimensional-arrays)

## Problem Statement

[Linear Kernel Function](https://www.deep-ml.com/problem/Linear%20Kernel)

Write a Python function `kernel_function` that computes the linear kernel between two input vectors `x1` and `x2`. The linear kernel is defined as the dot product (inner product) of two vectors.

## Example

```python
import numpy as np

x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

result = kernel_function(x1, x2)
print(result)
# Expected Output: 32
```

## Learn: Understanding the Linear Kernel

A kernel function in machine learning is used to measure the similarity between two data points in a higher-dimensional space without having to compute the coordinates of the points in that space explicitly. The linear kernel is one of the simplest and most commonly used kernel functions. It computes the dot product (or inner product) of two vectors.

### Mathematical Definition

The linear kernel between two vectors $\mathbf{x}_1$ and $\mathbf{x}_2$ is mathematically defined as:

$$ 
K(\mathbf{x}_1, \mathbf{x}_2) = \mathbf{x}_1 \cdot \mathbf{x}_2 = \sum_{i=1}^{n} x_{1,i} \cdot x_{2,i}
$$

Where $n$ is the number of features, and $x_{1,i}$ and $x_{2,i}$ are the components of the vectors $\mathbf{x}_1$ and $\mathbf{x}_2$ respectively.

The linear kernel is widely used in support vector machines (SVMs) and other machine learning algorithms for linear classification and regression tasks. It is computationally efficient and works well when the data is linearly separable.

### Characteristics

1. **Simplicity**: The linear kernel is straightforward to implement and compute.
2. **Efficiency**: It is computationally less expensive compared to other complex kernels like polynomial or RBF kernels.
3. **Interpretability**: The linear kernel is interpretable because it corresponds directly to the dot product, a well-understood operation in vector algebra.

## Solutions

### Custom Implementation

```python
import numpy as np

def kernel_function(x1: np.ndarray, x2: np.ndarray) -> int:
    # Step 1: List comprehension approach
    dot_sum = [x1[i] * x2[i] for i in range(len(x1))]
    return sum(dot_sum)

    # Normal approach (commented out)
    # dot_sum = 0
    # for i in range(len(x1)):
    #     dot_sum += x1[i] * x2[i]
    # return dot_sum
```

### NumPy Implementations

```python
import numpy as np

# Step 2: Using np.dot
def kernel_function(x1, x2):
    return np.dot(x1, x2)

# Step 3: Using np.inner
def kernel_function(x1, x2):
    return np.inner(x1, x2)
```

## Code Explanation

The custom implementation of `kernel_function` takes two NumPy arrays `x1` and `x2` as input and returns their dot product. There are two approaches shown:

1. **List Comprehension Approach (Step 1)**:
   - Use a list comprehension to multiply corresponding elements of `x1` and `x2`.
   - Sum up all the products using the `sum()` function.

2. **Normal Approach (commented out)**:
   - Initialize `dot_sum` to 0.
   - Iterate through the arrays, multiplying corresponding elements.
   - Accumulate the products in `dot_sum`.

The list comprehension approach is more concise and often faster for small to medium-sized arrays.

The NumPy implementations use built-in functions:

- `np.dot()` (Step 2): Computes the dot product of two arrays.
- `np.inner()` (Step 3): Computes the inner product of two arrays.

Both NumPy functions are more efficient and can handle multi-dimensional arrays, unlike the custom implementation.

## Note on Multidimensional Arrays

The custom implementation and `np.dot()` work correctly for 1D arrays, which is sufficient for the given test cases. However, `np.inner()` is the most versatile approach, as it can handle both 1D and 2D arrays correctly. For a more robust solution that works with multidimensional inputs, `np.inner()` is recommended.

When dealing with 2D arrays or matrices, `np.inner()` computes the inner product of vectors for the last dimension of `x1` and `x2`. This makes it more flexible and suitable for a wider range of input types.

