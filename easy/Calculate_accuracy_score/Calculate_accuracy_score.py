import numpy as np

def accuracy_score(y_true : list[int | float], y_pred : list[int | float]) -> float:
    # Your code here
    return final_value

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)