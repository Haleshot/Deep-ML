import numpy as np

# # Step 1
def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:  # type: ignore
    # Your code here
    y_pred = (X @ w).tolist()
    MSE = np.mean((y_true - y_pred)**2).tolist()
    reg = alpha * np.sum(w**2).tolist()
    return MSE + reg



X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)
