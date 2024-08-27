import numpy as np


def precision(y_true, y_pred):
    # Your code here
    pass


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
