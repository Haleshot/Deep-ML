import numpy as np

def shuffle_data(X : list[list[int]], y : list[list[int]], seed=None):
    # Your code here
    pass

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X=X, y=y)) # type: ignore