# Single Neuron (Easy) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Single Neuron Model](#learn-single-neuron-model)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [Code Explanation](#code-explanation)
- [Mathematical Background](#mathematical-background)

## Problem Statement

[Single Neuron](https://www.deep-ml.com/problem/Single%20Neuron)

Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, handling multidimensional input features. The function should take a list of feature vectors (each vector representing multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and bias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between the predicted probabilities and the true labels, both rounded to four decimal places.

## Example

```python
input: features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
output: ([0.4626, 0.4134, 0.6682], 0.3349)
reasoning: For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight, adding these up along with the bias, then applying the sigmoid function to produce a probability. The MSE is calculated as the average squared difference between each predicted probability and the corresponding true label.
```

## Learn: Single Neuron Model

This task involves a neuron model designed for binary classification with multidimensional input features, using the sigmoid activation function to output probabilities. It also involves calculating the mean squared error (MSE) to evaluate prediction accuracy.

The single neuron model with multidimensional input and sigmoid activation is a fundamental building block in neural networks. It's used for binary classification tasks where the goal is to predict the probability of an input belonging to one of two classes.

## Solutions

### Custom Implementation

```python
import math
import numpy as np

def single_neuron_model(
    features: list[list[float]], labels: list[int], weights: list[float], bias: float
) -> (list[float], float):  # type: ignore
    # Your code here

    # Step 1
    # print(features, "\n", weights)
    weighted_sum = []
    for i in features:
        c = 0
        temp = 0
        for j in i:
            temp += j * weights[c]
            c += 1
        weighted_sum.append(temp + bias)
    # print(weighted_sum)

    probabilities = [0] * len(weighted_sum)
    for i in range(len(weighted_sum)):
        probabilities[i] = round(1 / (1 + np.exp(-weighted_sum[i])), 4)
    # print(probabilities)
    mse = 0
    for i in range(len(labels)):
        mse += (labels[i] - probabilities[i]) ** 2
    # print(mse/len(labels))
    # weighted_sum = features * weights
    # print(weighted_sum)
    return probabilities, round(mse / len(labels), 4)

    # # Step 2:
    # probabilities = []
    # for feature_vector in features:
    #     z = (
    #         sum(weight * feature for weight, feature in zip(weights, feature_vector))
    #         + bias
    #     )
    #     prob = 1 / (1 + math.exp(-z))
    #     probabilities.append(round(prob, 4))

    # mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(
    #     labels
    # )
    # mse = round(mse, 4)

    # return probabilities, mse

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
print(single_neuron_model(features=features, labels=labels, weights=weights, bias=bias))
```

### Code Explanation

The `single_neuron_model` function implements a single neuron for binary classification. Here's a breakdown of the implementation:

1. The function initializes an empty list `weighted_sum` to store the weighted sum of features for each input vector.

2. It iterates through each feature vector in `features`:
   - For each feature in the vector, it multiplies it by the corresponding weight and accumulates the result in `temp`.
   - After processing all features in a vector, it adds the bias to `temp` and appends the result to `weighted_sum`.

3. The function then calculates the probabilities using the sigmoid activation function:
   - It initializes a list `probabilities` with zeros.
   - For each value in `weighted_sum`, it applies the sigmoid function (1 / (1 + e^(-x))) and rounds the result to 4 decimal places.

4. The Mean Squared Error (MSE) is calculated:
   - It iterates through the labels and probabilities, calculating the squared difference for each pair.
   - The sum of these squared differences is divided by the number of samples to get the average.

5. Finally, the function returns the list of probabilities and the rounded MSE.

The commented-out "Step 2" provides an alternative implementation using list comprehensions and the `zip` function. This approach is more concise but may be less intuitive for beginners.

## Mathematical Background

The single neuron model involves two main mathematical operations:

1. Neuron Output Calculation:

   $$z = \sum (weight_i \times feature_i) + bias$$
   $$probability = \frac{1}{1 + e^{-z}}$$

2. Mean Squared Error (MSE) Calculation:

   $$MSE = \frac{1}{n} \sum (predicted - true)^2$$

Where:
- $z$ is the sum of weighted inputs plus bias
- $probability$ is the sigmoid activation output
- $predicted$ are the probabilities after sigmoid activation
- $true$ are the true binary labels

This mathematical foundation allows the single neuron to perform binary classification by outputting probabilities and evaluating its performance using MSE.
