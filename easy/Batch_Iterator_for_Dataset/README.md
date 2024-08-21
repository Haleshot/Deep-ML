# Batch Iterator for Dataset (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Batch Iteration](#learn-understanding-batch-iteration)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Batch Iterator for Dataset](https://www.deep-ml.com/problem/Batch%20Iterator%20for%20Dataset)

Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

## Example

```python
X = np.array([[1, 2], 
              [3, 4], 
              [5, 6], 
              [7, 8], 
              [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
batch_iterator(X, y, batch_size)
output:
[[[[1, 2], [3, 4]], [1, 2]],
 [[[5, 6], [7, 8]], [3, 4]],
 [[[9, 10]], [5]]]
```

**Reasoning:**
The dataset X contains 5 samples, and we are using a batch size of 2. Therefore, the function will divide the dataset into 3 batches. The first two batches will contain 2 samples each, and the last batch will contain the remaining sample. The corresponding values from y are also included in each batch.

## Learn: Understanding Batch Iteration

Batch iteration is a common technique used in machine learning and data processing to handle large datasets more efficiently. Instead of processing the entire dataset at once, which can be memory-intensive, data is processed in smaller, more manageable batches.

Here's a step-by-step method to create a batch iterator:

1. **Determine the Number of Samples:** Calculate the total number of samples in the dataset.
2. **Iterate in Batches:** Loop through the dataset in increments of the specified batch size.
3. **Yield Batches:** For each iteration, yield a batch of samples from X and, if provided, the corresponding samples from y.

This method ensures efficient processing and can be used for both training and evaluation phases in machine learning workflows.

Mathematically, given a dataset $$X$$ with $$n$$ samples and a batch size of $$b$$, the number of batches $$N$$ is calculated as:

$$N = \left\lceil\frac{n}{b}\right\rceil$$

Where $$\lceil \cdot \rceil$$ denotes the ceiling function.

## Solutions

### Custom Implementation

```python
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = len(X) # Rows of X array
    batches = (n_samples + batch_size - 1) // batch_size  # Calculate the number of batches
    # print(batches)
    result = []

    for i in range(batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, n_samples)
        
        if y is not None:
            batch_X = X[start_idx:end_idx].tolist()
            batch_y = y[start_idx:end_idx].tolist()
            result.append([batch_X, batch_y])
        else:
            batch_X = X[start_idx:end_idx].tolist()
            result.append(batch_X)
    
    return result

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))

print(batch_iterator(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), batch_size=3))
```

### NumPy Implementation

```python
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = X.shape[0]
    batches = []
    for i in np.arange(0, n_samples, batch_size):
        begin, end = i, min(i+batch_size, n_samples)
        if y is not None:
            batches.append([X[begin:end], y[begin:end]])
        else:
            batches.append(X[begin:end])
    return batches

# Usage remains the same as the custom implementation
```

## Code Explanation

Both implementations of the `batch_iterator` function take three parameters:

- `X`: a numpy array representing the input samples
- `y`: an optional numpy array representing the labels (default is None)
- `batch_size`: an integer specifying the size of each batch (default is 64)

### Custom Implementation

1. Calculate the number of samples (`n_samples`) in the input array `X`.
2. Calculate the number of batches using integer division, ensuring all samples are covered.
3. Initialize an empty list `result` to store the batches.
4. Iterate through the range of batches:
   - Calculate the start and end indices for each batch.
   - If `y` is provided, create batches of `[X, y]` pairs.
   - If `y` is not provided, create batches of `X` only.
   - Append each batch to the `result` list.
5. Return the `result` list containing all batches.

### NumPy Implementation

1. Get the number of samples from the shape of `X`.
2. Initialize an empty list `batches` to store the results.
3. Use `np.arange()` to create an iterator over the sample indices with the given `batch_size`.
4. For each iteration:
   - Calculate the begin and end indices for the current batch.
   - If `y` is provided, append `[X[begin:end], y[begin:end]]` to `batches`.
   - If `y` is not provided, append `X[begin:end]` to `batches`.
5. Return the `batches` list.

Both implementations achieve the same result, but the NumPy version leverages NumPy's built-in functions for potentially better performance, especially with larger datasets. The custom implementation provides more explicit control over the batching process and may be easier to understand for those less familiar with NumPy.
