import numpy as np


# Step 1
def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    # Your code here, make sure to round
    mat = np.dot(np.transpose(X), X)
    mat = np.linalg.inv(mat)
    mult = np.dot(np.transpose(X), y)
    theta = np.dot(mat, mult)
    return np.round(theta, 4)


# # Step 2
# def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
#     # Your code here, make sure to round
#     X = np.array(X) # type: ignore
#     y = np.array(y).reshape(-1, 1) # type: ignore
#     # print(X, "\n", y)
#     X_transpose = X.T # type: ignore
#     theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
#     theta = np.round(theta, 4).flatten().tolist()
#     return theta

X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X=X, y=y))  # type: ignore
