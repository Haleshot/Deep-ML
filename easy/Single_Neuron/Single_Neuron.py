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
