import numpy as np


# # Step 1
def linear_regression_gradient_descent(X, y, alpha, num_iterations) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Parameters:
    X : numpy.ndarray
        Feature matrix including a column of ones for the intercept.
    y : numpy.ndarray
        Target vector.
    alpha : float
        Learning rate.
    num_iterations : int
        Number of iterations for gradient descent.

    Returns:
    numpy.ndarray
        Coefficients of the linear regression model rounded to four decimal places.
    """
    # Number of training examples
    m = len(y)

    # Initialize weights (coefficients) to zeros
    theta = np.zeros(X.shape[1])

    for i in range(num_iterations):
        # Compute predictions
        predictions = X.dot(theta)

        # Compute the error (difference between predictions and actual values)
        errors = predictions - y

        # Compute the gradient of the cost function with respect to each weight
        gradient = (1 / m) * X.T.dot(errors)

        # Update the weights by moving in the opposite direction of the gradient
        theta -= alpha * gradient

        # (Optional) Print the cost function value to monitor the convergence
        # cost = (1 / (2 * m)) * np.sum(errors ** 2)
        # print(f"Iteration {i+1}: Cost {cost:.4f}")

    # Round the coefficients to four decimal places
    theta = np.round(theta, 4)

    return theta


# # Step 2:
# def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
#     m, n = X.shape
#     theta = np.zeros((n, 1))
#     for _ in range(iterations):
#         predictions = X @ theta
#         errors = predictions - y.reshape(-1, 1)
#         updates = X.T @ errors / m
#         theta -= alpha * updates
#     return np.round(theta.flatten(), 4)


# Testing
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000
print(linear_regression_gradient_descent(X=X, y=y, alpha=alpha, num_iterations=iterations))  # type: ignore
