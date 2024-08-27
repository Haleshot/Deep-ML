import numpy as np

# # Step 1
# def precision(y_true, y_pred):
#     # Your code here
#     tp, fp = 0, 0
#     for i in range(len(y_pred)):
#         if (y_pred[i] == y_true[i]) and y_true[i] == 1:
#             tp += 1
#         elif (y_pred[i] != y_true[i]) and y_pred[i] == 1:
#             fp += 1
#     return tp/(tp + fp)


# # Step 2
def precision(y_true, y_pred):
    tp, fp = np.sum((y_true == 1) & (y_pred == 1)), np.sum(
        (y_true == 0) & (y_pred == 1)
    )
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
