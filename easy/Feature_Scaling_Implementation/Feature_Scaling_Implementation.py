import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    return standardized_data, normalized_data

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))