import numpy as np


# # Step 1
def to_categorical(x, n_col=None):
    # Your code here
    if n_col is None:
        n_col = x.max() + 1  # Determine the number of columns from the input array

    one_hot = np.zeros((x.size, n_col), dtype=int)
    # print(one_hot)
    one_hot[np.arange(x.size), x] = 1

    return one_hot


# # Step 2
# def to_categorical(x, n_col=None):
#     # One-hot encoding of nominal values
#     # If n_col is not provided, determine the number of columns from the input array
#     if not n_col:
#         n_col = np.amax(x) + 1
#     # Initialize a matrix of zeros with shape (number of samples, n_col)
#     one_hot = np.zeros((x.shape[0], n_col))
#     # Set the appropriate elements to 1
#     one_hot[np.arange(x.shape[0]), x] = 1
#     return one_hot


x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
