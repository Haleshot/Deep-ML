import numpy as np
import random

# Step 1
def shuffle_data(X : list[list[int]], y : list[int], seed=None):
    if seed:
        np.random.seed(seed)
    x_len = len(X)
    indices = list(range(x_len))

    random.shuffle(indices)

    finalX = [X[i] for i in indices]
    finaly = [y[i] for i in indices]

    return finalX, finaly
    

# # Step 2
# def shuffle_data(X : list[list[int]], y : list[int], seed=None):
#     if seed:
#         np.random.seed(seed)
#     idx = np.arange(X.shape[0]) # type: ignore
#     np.random.shuffle(idx)
#     return X[idx], y[idx]
    

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X=X, y=y)) # type: ignore