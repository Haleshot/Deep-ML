import numpy as np


def to_categorical(x: np.ndarray, n_col=None):
    # Your code here
    results = [[] for _ in range(max(x) + 1) for _ in range(len(x))]
    
    print(results)
    pass


x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
