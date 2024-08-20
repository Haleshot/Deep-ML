import numpy as np


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray): # type: ignore
    # Your code here
    standardized_data, normalized_data = [[] for _ in range(len(data))], [[] for _ in range(len(data))]
    for i in range(len(data)):
        std_dev = np.std(data[i])
        mu = np.mean(data[i])
        standardized_data[i].append((data[i] - mu) / std_dev)
        
    return standardized_data, normalized_data


data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data=data))