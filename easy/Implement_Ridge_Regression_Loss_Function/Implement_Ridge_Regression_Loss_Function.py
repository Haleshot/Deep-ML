import numpy as np


# # Step 1:
def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    y_pred = []
    for i in range(len(X)):
        temp = 0
        for j in range(len(w)):
            temp += X[i][j] * w[j]
        y_pred.append(temp)
        # y_pred[i] += [i for i in y_pred]

    # print(X @ w)
    MSE = sum((((y_true - y_pred) ** 2) / len(X)).tolist())
    sum_w = sum([i**2 for i in w])
    reg = alpha * sum_w
    # print(MSE, reg)
    return MSE + reg


# # Step 2
# def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:  # type: ignore
#     # Your code here
#     y_pred = (X @ w).tolist()
#     MSE = np.mean((y_true - y_pred)**2).tolist()
#     reg = alpha * np.sum(w**2).tolist()
#     # print(MSE, reg)
#     return MSE + reg


X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)
