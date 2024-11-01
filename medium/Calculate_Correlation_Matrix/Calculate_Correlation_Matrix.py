import numpy as np


def calculate_correlation_matrix(X, Y=None):
    # Your code here
    if Y:
        pass
    cov = np.cov(X)
    std = np.std(X)
    corr = cov / std * std
    return corr


X = np.array([[1, 2], [3, 4], [5, 6]])

output = calculate_correlation_matrix(X=X)
print(output)
