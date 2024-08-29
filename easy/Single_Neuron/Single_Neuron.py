import math


def single_neuron_model(
    features: list[list[float]], labels: list[int], weights: list[float], bias: float
) -> (list[float], float):
    # Your code here
    return probabilities, mse


features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
print(single_neuron_model(features=features, labels=labels, weights=weights, bias=bias))