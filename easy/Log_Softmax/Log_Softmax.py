import numpy as np


# # Step 1
def log_softmax(scores: list[int | float]) -> np.ndarray:
    # softmax = [np.exp(i)/np.sum(scores) for i in scores]
    total_log = np.sum([np.exp(i - max(scores)) for i in scores])
    # print(total_log)
    log_softmax = [
        scores[i] - max(scores) - np.log(total_log) for i in range(len(scores))
    ]
    # print(log_softmax)
    # print(np.exp(2))
    return log_softmax  # type: ignore


# # Step 2
# def log_softmax(scores: list) -> np.ndarray:
#     # Subtract the maximum value for numerical stability
#     scores = scores - np.max(scores)
#     return scores - np.log(np.sum(np.exp(scores)))

A = np.array([1, 2, 3])
print(log_softmax(A))  # type: ignore
