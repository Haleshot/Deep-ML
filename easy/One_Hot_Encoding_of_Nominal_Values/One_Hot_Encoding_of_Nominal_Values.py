import numpy as np


def to_categorical(x: np.ndarray, n_col=None):
    # Your code here
    pass


x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
