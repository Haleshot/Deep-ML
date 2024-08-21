import numpy as np
import math


# # Step 1
# def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):  # type: ignore
#     # Standardization

#     std = np.std(data, axis=0)
#     mean = np.mean(data, axis=0)
#     print(std, mean)
#     standardized_data = (data - mean) / std

#     # MinMax normalization data
#     min_val = np.min(data, axis=0)
#     max_val = np.max(data, axis=0)
#     print(min_val, max_val)
#     normalized_data = (data - min_val) / (max_val - min_val)

#     return (
#         np.round(standardized_data, 4).tolist(),
#         np.round(normalized_data, 4).tolist(),
#     )


# # Step 2
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):  # type: ignore
    # Standardization
    standardized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # MinMax normalization
    normalized_data = (data - np.min(data, axis=0)) / (
        np.max(data, axis=0) - np.min(data, axis=0)
    )

    return (
        np.round(standardized_data, 4).tolist(),
        np.round(normalized_data, 4).tolist(),
    )


data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))
