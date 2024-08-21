import numpy as np
import math


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):  # type: ignore
    # Your code here
    # Standardization

    std = np.std(data, axis=0)
    mean = np.mean(data, axis=0)
    standardized_data = (data - mean) / std

    # MinMax normalization data
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)

    return np.round(standardized_data, 4).tolist(), np.round(normalized_data, 4).tolist()


data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))
