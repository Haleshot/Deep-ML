# Softmax Activation Function Implementation (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Understanding the Softmax Activation Function](#learn-understanding-the-softmax-activation-function)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[Softmax Activation Function Implementation](https://www.deep-ml.com/problem/Softmax%20Activation%20Function%20Implementation)

Write a Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list, each rounded to four decimal places.

## Example

```python
input: scores = [1, 2, 3]
output: [0.0900, 0.2447, 0.6652]
reasoning: The softmax function converts a list of values into a probability distribution. The probabilities are proportional to the exponential of each element divided by the sum of the exponentials of all elements in the list.
```

## Learn: Understanding the Softmax Activation Function

The softmax function is a generalization of the sigmoid function and is used in the output layer of a neural network model that handles multi-class classification tasks.

### Mathematical Definition

The softmax function is mathematically represented as:

$$
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}
$$

### Characteristics

- **Output Range**: Each output value is between 0 and 1, and the sum of all outputs is 1.
- **Purpose**: It transforms scores into probabilities, which are easier to interpret and are useful for classification.

This function is essential for models where the output needs to represent a probability distribution across multiple classes.

## Solutions

### Custom Implementation

```python
import math

def softmax(scores: list[int | float]) -> list[float]:
    sum_exp_scores = sum([math.exp(i) for i in scores])
    probabilities = [round(math.exp(i) / sum_exp_scores, 4) for i in scores]
    return probabilities

scores = [1, 2, 3]
print(softmax(scores=scores))
```

### NumPy Implementation

```python
import numpy as np

def softmax(scores: list[int | float]) -> list[float]:
    sum_exp_scores = sum([np.exp(i) for i in scores])
    probabilities = [round(np.exp(i)/sum_exp_scores, 4) for i in scores]
    return probabilities

scores = [1, 2, 3]
print(softmax(scores=scores))
```

## Code Explanation

Both implementations of the `softmax` function take a list of scores as input and return a list of probabilities. The function works as follows:

1. Calculate the exponential of each score in the input list.
2. Sum up all the exponential values.
3. Divide each exponential value by the sum to get the softmax probabilities.
4. Round each probability to four decimal places.

The custom implementation uses Python's built-in `math` module, while the NumPy implementation uses the `numpy` library. Both approaches yield the same results, but the NumPy version might be more efficient for larger datasets due to its optimized array operations.

The main difference between the two implementations is the use of `math.exp()` in the custom version versus `np.exp()` in the NumPy version. Both functions compute the exponential of a given number, but `np.exp()` can handle array inputs more efficiently.

Both implementations demonstrate a clear understanding of the softmax function and provide an efficient way to compute softmax probabilities for a given list of scores.
