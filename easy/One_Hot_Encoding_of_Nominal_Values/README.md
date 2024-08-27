# One-Hot Encoding of Nominal Values (easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding One-Hot Encoding](#learn-understanding-one-hot-encoding)
- [Solutions](#solutions)
  - [Implementation 1](#implementation-1)
  - [Implementation 2](#implementation-2)
- [Code Explanation](#code-explanation)

## Problem Statement

[One-Hot Encoding of Nominal Values](https://www.deep-ml.com/problem/One-Hot%20Encoding%20of%20Nominal%20Values)

Write a Python function to perform one-hot encoding of nominal values. The function should take in a 1D numpy array `x` of integer values and an optional integer `n_col` representing the number of columns for the one-hot encoded array. If `n_col` is not provided, it should be automatically determined from the input array.

## Example

```python
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]]

Reasoning:
Each element in the input array is transformed into a one-hot encoded vector,
where the index corresponding to the value in the input array is set to 1, 
and all other indices are set to 0.
```

## Learn: Understanding One-Hot Encoding

One-hot encoding is a method used to represent categorical variables as binary vectors. This technique is useful in machine learning when dealing with categorical data that has no ordinal relationship.

In one-hot encoding, each category is represented by a binary vector with a length equal to the number of categories. The vector has a value of 1 at the index corresponding to the category and 0 at all other indices.

For example, if you have three categories: 0, 1, and 2, the one-hot encoded vectors would be:

- 0: [1, 0, 0]
- 1: [0, 1, 0]
- 2: [0, 0, 1]

This method ensures that the model does not assume any ordinal relationship between categories, which is crucial for many machine learning algorithms. The one-hot encoding process can be mathematically represented as follows:

Given a category $x_i$ from a set of categories $C$, the one-hot encoded vector $\mathbf{v}$ is:

$$ \mathbf{v}_i = 
\begin{cases} 
1 & \text{if } i = x_i \\
0 & \text{otherwise}
\end{cases}
$$

This vector $\mathbf{v}$ will have a length equal to the number of unique categories.

## Solutions

### Implementation 1

```python
import numpy as np

def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = x.max() + 1  # Determine the number of columns from the input array

    one_hot = np.zeros((x.size, n_col), dtype=int)
    one_hot[np.arange(x.size), x] = 1

    return one_hot
```

### Implementation 2

```python
import numpy as np

def to_categorical(x, n_col=None):
    # One-hot encoding of nominal values
    # If n_col is not provided, determine the number of columns from the input array
    if not n_col:
        n_col = np.amax(x) + 1
    # Initialize a matrix of zeros with shape (number of samples, n_col)
    one_hot = np.zeros((x.shape[0], n_col))
    # Set the appropriate elements to 1
    one_hot[np.arange(x.shape[0]), x] = 1
    return one_hot
```

## Code Explanation

Both implementations achieve the same goal of performing one-hot encoding, but they have slight differences in their approach:

### Implementation 1:

1. If `n_col` is not provided, it calculates the number of columns using `x.max() + 1`.
2. It initializes a zero matrix `one_hot` with dimensions `(x.size, n_col)` and dtype `int`.
3. It uses NumPy's advanced indexing to set the appropriate elements to 1.

### Implementation 2:

1. If `n_col` is not provided, it calculates the number of columns using `np.amax(x) + 1`.
2. It initializes a zero matrix `one_hot` with dimensions `(x.shape[0], n_col)` as float (default NumPy dtype).
3. It uses the same NumPy advanced indexing technique to set the appropriate elements to 1.

The main differences are:
- Implementation 1 uses `x.max()`, while Implementation 2 uses `np.amax(x)` to determine the number of columns.
- Implementation 1 explicitly sets the dtype to `int`, while Implementation 2 uses the default float dtype.
- Implementation 1 uses `x.size` for the number of rows, while Implementation 2 uses `x.shape[0]`.

Both implementations efficiently use NumPy's vectorized operations to perform the one-hot encoding, making them fast and suitable for large arrays. The choice between the two would depend on specific requirements regarding dtype and any potential integration with existing code.
