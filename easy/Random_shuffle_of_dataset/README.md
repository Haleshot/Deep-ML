# Random Shuffle of Dataset (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Dataset Shuffling](#learn-understanding-dataset-shuffling)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Random Shuffle of Dataset](https://www.deep-ml.com/problem/Random%20Shuffle%20of%20Dataset)

Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. The function should have an optional seed parameter for reproducibility.

## Example

```python
X = np.array([[1, 2], 
              [3, 4], 
              [5, 6], 
              [7, 8]])
y = np.array([1, 2, 3, 4])
output: (array([[5, 6],
                [1, 2],
                [7, 8],
                [3, 4]]), 
         array([3, 1, 4, 2]))
```

## Learn: Understanding Dataset Shuffling

Random shuffling of a dataset is a common preprocessing step in machine learning to ensure that the data is randomly distributed before training a model. This helps to avoid any potential biases that may arise from the order in which data is presented to the model.

Here's a step-by-step method to shuffle a dataset:

1. Generate a Random Index Array: Create an array of indices corresponding to the number of samples in the dataset.
2. Shuffle the Indices: Use a random number generator to shuffle the array of indices.
3. Reorder the Dataset: Use the shuffled indices to reorder the samples in both X and y.

This method ensures that the correspondence between X and y is maintained after shuffling.

Mathematically, if we have a dataset $D = \{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\}$, where $x_i$ are input features and $y_i$ are corresponding labels, shuffling can be represented as:

$$D_{shuffled} = \{(x_{\pi(1)}, y_{\pi(1)}), (x_{\pi(2)}, y_{\pi(2)}), ..., (x_{\pi(n)}, y_{\pi(n)})\}$$

Where $\pi$ is a random permutation of the indices $\{1, 2, ..., n\}$.

## Solutions

### Custom Implementation

```python
import numpy as np
import random

def shuffle_data(X: list[list[int]], y: list[int], seed=None):
    if seed:
        np.random.seed(seed)  # Set the random seed for reproducibility

    x_len = len(X)
    indices = list(range(x_len))  # Create a list of indices from 0 to len(X)-1
    
    np.random.shuffle(indices)  # Shuffle the list of indices

    finalX = [X[i] for i in indices]  # Rearrange X according to the shuffled indices
    finaly = [y[i] for i in indices]  # Rearrange y according to the shuffled indices

    return finalX, finaly

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X=X, y=y))
```

### NumPy Implementation

```python
import numpy as np

def shuffle_data(X : list[list[int]], y : list[int], seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X=X, y=y))
```

## Code Explanation

Both implementations aim to shuffle the dataset while maintaining the correspondence between X and y. Let's break down each approach:

### Custom Implementation

1. The function `shuffle_data` takes three parameters: `X` (the feature matrix), `y` (the label array), and an optional `seed` for reproducibility.
2. If a seed is provided, it's set using `np.random.seed(seed)`.
3. We create a list of indices `indices` ranging from 0 to the length of X minus 1.
4. The `np.random.shuffle(indices)` function is used to randomly shuffle these indices.
5. We then create new lists `finalX` and `finaly` by rearranging the elements of X and y according to the shuffled indices.
6. The function returns the shuffled `finalX` and `finaly`.

This method explicitly creates the shuffled indices and rearranges the data, which can be helpful for understanding the process.

### NumPy Implementation

1. The function signature is the same as the custom implementation.
2. If a seed is provided, it's set using `np.random.seed(seed)`.
3. We create an array of indices using `np.arange(X.shape[0])`.
4. The `np.random.shuffle(idx)` function is used to randomly shuffle these indices in-place.
5. We return `X[idx]` and `y[idx]`, which uses NumPy's advanced indexing to rearrange the data.

This method leverages NumPy's efficient array operations and can be faster, especially for larger datasets.

Both methods achieve the same result of randomly shuffling the dataset while maintaining the relationship between features and labels. The choice between them might depend on specific requirements, such as performance needs or integration with existing code.
