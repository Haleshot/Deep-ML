# Calculate Accuracy Score (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Accuracy Score](#learn-understanding-accuracy-score)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Calculate Accuracy Score](https://www.deep-ml.com/problem/Calculate%20Accuracy%20Score)

Write a Python function to calculate the accuracy score of a model's predictions. The function should take in two 1D numpy arrays: `y_true`, which contains the true labels, and `y_pred`, which contains the predicted labels. It should return the accuracy score as a float.

## Example

```python
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)
# Output:
# 0.8333333333333334

Reasoning:
The function compares the true labels with the predicted labels and calculates the ratio of correct predictions to the total number of predictions. In this example, there are 5 correct predictions out of 6, resulting in an accuracy score of 0.8333333333333334.
```

## Learn: Understanding Accuracy Score

Accuracy is a metric used to evaluate the performance of a classification model. It is defined as the ratio of the number of correct predictions to the total number of predictions made. Mathematically, accuracy is given by:

$$\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}$$

In this problem, you will write a function to calculate the accuracy score given the true labels and the predicted labels. The function will compare the two arrays and compute the accuracy as the proportion of matching elements.

Accuracy is a straightforward and commonly used metric for classification tasks. It provides a quick way to understand how well a model is performing, but it may not always be the best metric, especially for imbalanced datasets.

## Solutions

### Custom Implementation

```python
import numpy as np

def accuracy_score(y_true : list[int | float], y_pred : list[int | float]) -> float:
    # Your code here
    c = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            c += 1
    return c/len(y_true)

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)
```

### NumPy Implementation

```python
import numpy as np

def accuracy_score(y_true : list[int | float], y_pred : list[int | float]) -> float:
    # Your code here
    accuracy = np.sum(y_true == y_pred, axis=0)/len(y_pred)
    return accuracy

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)
```

## Code Explanation

Both implementations of the `accuracy_score` function take two parameters:

- `y_true`: a 1D numpy array containing the true labels
- `y_pred`: a 1D numpy array containing the predicted labels

The function returns a float value representing the accuracy score.

### Custom Implementation

The custom implementation works as follows:

1. Initialize a counter `c` to 0.
2. Iterate through the indices of `y_true` and `y_pred`.
3. For each index, if the elements in `y_true` and `y_pred` are equal, increment the counter `c`.
4. After the loop, return the ratio of `c` to the total number of elements.

This implementation directly applies the mathematical definition of accuracy by counting the number of correct predictions and dividing by the total number of predictions.

### NumPy Implementation

The NumPy implementation utilizes NumPy's array operations:

1. Use `y_true == y_pred` to create a boolean array where `True` represents correct predictions.
2. Use `np.sum()` to count the number of `True` values (correct predictions).
3. Divide the sum by the total number of predictions (`len(y_pred)`).

This implementation is more concise and potentially more efficient, especially for larger arrays, as it leverages NumPy's optimized array operations.

Both implementations will produce the same result, but the NumPy version may be preferred in scenarios where performance is critical or when working with larger datasets that are already in NumPy array format.
