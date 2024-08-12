import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    mat = np.dot(np.transpose(X), X)
    mat = np.linalg.inv(mat)
    mult = np.dot(np.transpose(X), y)
    theta = np.dot(mat, mult)
    return np.round(theta, 2)

X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X=X, y=y))