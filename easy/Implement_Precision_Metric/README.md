# Implement Precision Metric (easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding Precision in Classification](#learn-understanding-precision-in-classification)
- [Solutions](#solutions)
  - [Step 1: Custom Implementation](#step-1-custom-implementation)
  - [Step 2: NumPy Implementation](#step-2-numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Implement Precision Metric](https://www.deep-ml.com/problem/Precision%20Metric)

Write a Python function `precision` that calculates the precision metric given two numpy arrays: `y_true` and `y_pred`. The `y_true` array contains the true binary labels, and the `y_pred` array contains the predicted binary labels. Precision is defined as the ratio of true positives to the sum of true positives and false positives.

## Example

```python
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
# Expected Output: 1.0
```

## Learn: Understanding Precision in Classification

Precision is a key metric used in the evaluation of classification models, particularly in binary classification. It provides insight into the accuracy of the positive predictions made by the model.

### Mathematical Definition

Precision is defined as the ratio of true positives (TP) to the sum of true positives and false positives (FP):

$$ \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} $$

Where:
- True Positives (TP): The number of positive samples that are correctly identified as positive.
- False Positives (FP): The number of negative samples that are incorrectly identified as positive.

### Characteristics of Precision

- Range: Precision ranges from 0 to 1, where 1 indicates perfect precision (no false positives) and 0 indicates no true positives.
- Interpretation: High precision means that the model has a low false positive rate, meaning it rarely labels negative samples as positive.
- Use Case: Precision is particularly useful when the cost of false positives is high, such as in medical diagnosis or fraud detection.

## Solutions

### Step 1: Custom Implementation

```python
def precision(y_true, y_pred):
    tp, fp = 0, 0
    for i in range(len(y_pred)):
        if (y_pred[i] == y_true[i]) and y_true[i] == 1:
            tp += 1
        elif (y_pred[i] != y_true[i]) and y_pred[i] == 1:
            fp += 1
    return tp/(tp + fp)
```

### Step 2: NumPy Implementation

```python
import numpy as np

def precision(y_true, y_pred):
    tp, fp = np.sum((y_true == 1) & (y_pred == 1)), np.sum((y_true == 0) & (y_pred == 1))
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
```

## Code Explanation

### Step 1: Custom Implementation

This implementation uses a traditional loop-based approach to calculate precision:

1. Initialize counters `tp` (true positives) and `fp` (false positives) to 0.
2. Iterate through the arrays `y_true` and `y_pred` simultaneously:
   - If `y_pred[i] == y_true[i] == 1`, increment `tp` (true positive).
   - If `y_pred[i] != y_true[i]` and `y_pred[i] == 1`, increment `fp` (false positive).
3. Calculate and return the precision as `tp / (tp + fp)`.

This method is straightforward and easy to understand but may be less efficient for large datasets compared to vectorized operations.

### Step 2: NumPy Implementation

The NumPy implementation leverages efficient array operations:

1. `tp = np.sum((y_true == 1) & (y_pred == 1))`: Calculates true positives using element-wise comparison and logical AND.
2. `fp = np.sum((y_true == 0) & (y_pred == 1))`: Calculates false positives similarly.
3. `return tp / (tp + fp) if (tp + fp) > 0 else 0.0`: Computes precision, handling the case of zero division.

This implementation is more efficient, especially for large arrays, as it utilizes NumPy's vectorized operations. It also includes a check to avoid division by zero, returning 0.0 if there are no positive predictions.

Both implementations correctly calculate the precision metric, but the NumPy version is generally preferred for its efficiency and built-in handling of edge cases.
