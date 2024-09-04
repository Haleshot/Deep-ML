# # # Step 1
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    means = [sum(feature) / n_observations for feature in vectors]
    # print(covariance_matrix, "\n", means)

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n_observations)
            ) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance  # type: ignore

    return covariance_matrix  # type: ignore


# # Step 2
# import numpy as np
# def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
#     # Convert the input list to a NumPy array for easier mathematical operations
#     data = np.array(vectors)

#     # Calculate the mean of each feature
#     means = np.mean(data, axis=1)

#     # Center the data by subtracting the mean of each feature
#     centered_data = data - means[:, np.newaxis]

#     # Number of observations (columns)
#     n = data.shape[1]

#     # Calculate the covariance matrix
#     covariance_matrix = np.dot(centered_data, centered_data.T) / (n - 1)

#     return covariance_matrix.tolist()

# Example usage
vectors = [[1, 2, 3], [4, 5, 6]]
result = calculate_covariance_matrix(vectors)  # type: ignore
print(result)
