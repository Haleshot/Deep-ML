import numpy as np
import random

# # Step 1
# def shuffle_data(X : list[list[int]], y : list[int], seed=None):
#     if seed:
#         np.random.seed(seed)
#     x_len, y_len = len(X), len(y) - 1
#     x_arr, y_arr = [], []
#     # x_arr, y_arr = [random.randint(0, x_len) for _ in range(x_len)], [random.randint(0, y_len) for _ in range(y_len)]
#     i = 0
#     while i < x_len:
#         temp =  random.randint(0, x_len - 1)
#         if temp not in x_arr:
#             x_arr.append(temp)
#             i += 1
#     finalX, finaly = [], []
#     # print(x_arr)
#     for i in range(len(x_arr)):
#         finalX.append(X[x_arr[i]])
#         finaly.append(y[x_arr[i]])

#     return finalX, finaly
    

# # Step 2
def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]
    

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X=X, y=y)) # type: ignore