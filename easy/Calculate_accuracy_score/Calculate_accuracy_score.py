import numpy as np


# Step 1
def accuracy_score(y_true: list[int | float], y_pred: list[int | float]) -> float:
    # Your code here
    c = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            c += 1
    return c / len(y_true)


# # Step 2:
# def accuracy_score(y_true : list[int | float], y_pred : list[int | float]) -> float:
#     # Your code here
#     accuracy = np.sum(y_true == y_pred, axis=0)/len(y_pred)
#     return accuracy


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)
