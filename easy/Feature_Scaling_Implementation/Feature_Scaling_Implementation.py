import numpy as np
import math


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):  # type: ignore
    # Your code here
    # Standardization

    std = np.std(data, axis=0)
    mean = np.mean(data, axis=0)
    standardized_data = (data - mean) / std

    # MinMax normalization data

    return standardized_data, normalized_data


data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))
