# Feature Scaling Implementation (easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Feature Scaling Techniques](#learn-feature-scaling-techniques)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Feature Scaling Implementation](https://www.deep-ml.com/problem/Feature%20Scaling%20Implementation)

Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.

## Example

```python
Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]])
        output: ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
        reasoning: Standardization rescales the feature to have a mean of 0 and a standard deviation of 1.
        Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value
        maps to 0 and the maximum to 1.
```

## Learn: Feature Scaling Techniques

Feature Scaling is crucial in many machine learning algorithms that are sensitive to the magnitude of features. This includes algorithms that use distance measures like k-nearest neighbors and gradient descent-based algorithms like linear regression.

**Standardization:**
Standardization (or Z-score normalization) is the process where the features are rescaled so that they have the properties of a standard normal distribution with a mean of zero and a standard deviation of one:

$$ z = \frac{(x - \mu)}{\sigma} $$

where $x$ is the original feature, $\mu$ is the mean of that feature, and $\sigma$ is the standard deviation.

**Min-Max Normalization:**
Min-max normalization rescales the feature to a fixed range, typically 0 to 1, or it can be shifted to any range $[min, max]$ by transforming the data according to the formula:

$$ x' = \frac{(x - \text{min}(x))}{(\text{max}(x) - \text{min}(x))} \times (\text{max} - \text{min}) + \text{min} $$

where $x$ is the original value, $\text{min}(x)$ is the minimum value for that feature, $\text{max}(x)$ is the maximum value, and $\text{min}$ and $\text{max}$ are the new minimum and maximum values for the scaled data.

Implementing these scaling techniques will ensure that the features contribute equally to the development of the model and improve the convergence speed of learning algorithms.

## Solutions

### Custom Implementation

```python
import numpy as np
import math


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):  # type: ignore
    # Standardization
    std = np.std(data, axis=0)
    mean = np.mean(data, axis=0)
    standardized_data = (data - mean) / std

    # MinMax normalization data
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)

    return (
        np.round(standardized_data, 4).tolist(),
        np.round(normalized_data, 4).tolist(),
    )


data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))
```

### NumPy Implementation

```python
import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Standardization
    standardized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # MinMax normalization
    normalized_data = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

    return (
        np.round(standardized_data, 4).tolist(),
        np.round(normalized_data, 4).tolist(),
    )

# Usage remains the same as the custom implementation
```

## Code Explanation

The custom implementation of the `feature_scaling` function takes a 2D NumPy array `data` as input, where each row represents a data sample and each column represents a feature.

The function performs the following steps:

1. **Standardization:**
   - It calculates the standard deviation `std` and the mean `mean` of the input data along the column axis (axis 0).
   - It then subtracts the mean from the data and divides it by the standard deviation to get the standardized data.

2. **Min-Max Normalization:**
   - It calculates the minimum `min_val` and maximum `max_val` values of the input data along the column axis (axis 0).
   - It then subtracts the minimum value from the data and divides it by the difference between the maximum and minimum values to get the normalized data.

3. The function then rounds the standardized and normalized data to the nearest 4th decimal place using the `np.round()` function and converts the resulting NumPy arrays to lists before returning them.

The NumPy implementation follows a similar approach but utilizes the built-in NumPy functions `np.mean()`, `np.std()`, `np.min()`, and `np.max()` to perform the feature scaling operations. This version is more concise and potentially more efficient, especially for larger datasets, as it leverages NumPy's optimized array operations.

Both implementations produce the same result, but the NumPy version may be preferred in scenarios where performance is critical or when working with larger datasets that are already in NumPy array format.
