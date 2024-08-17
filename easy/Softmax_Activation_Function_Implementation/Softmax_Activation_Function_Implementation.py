import math
import numpy as np


# Step 1
def softmax(scores: list[int | float]) -> list[float]:
    # Your code here
    sum_exp_scores = sum([math.exp(i) for i in scores])
    probabilities = [round(math.exp(i) / sum_exp_scores, 4) for i in scores]
    return probabilities


# # Step 2
# def softmax(scores: list[int | float]) -> list[float]:
#     # Your code here
#     sum_exp_scores = sum([np.exp(i) for i in scores])
#     probabilities = [round(np.exp(i)/sum_exp_scores, 4) for i in scores]
#     return probabilities

scores = [1, 2, 3]
print(softmax(scores=scores))  # type: ignore
