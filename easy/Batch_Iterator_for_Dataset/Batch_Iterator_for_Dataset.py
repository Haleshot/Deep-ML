# # Step 1
import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    n_samples = len(X)  # Rows of X array
    batches = (
        n_samples + batch_size - 1
    ) // batch_size  # Calculate the number of batches
    # print(batches)
    result = []

    for i in range(batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, n_samples)

        if y is not None:
            batch_X = X[start_idx:end_idx].tolist()
            batch_y = y[start_idx:end_idx].tolist()
            result.append([batch_X, batch_y])
        else:
            batch_X = X[start_idx:end_idx].tolist()
            result.append(batch_X)

    return result


# # Step 2
# def batch_iterator(X, y=None, batch_size=64):
#     n_samples = X.shape[0]
#     batches = []
#     for i in np.arange(0, n_samples, batch_size):
#         begin, end = i, min(i+batch_size, n_samples)
#         if y is not None:
#             batches.append([X[begin:end], y[begin:end]])
#         else:
#             batches.append( X[begin:end])
#     return batches

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))

print(batch_iterator(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), batch_size=3))
