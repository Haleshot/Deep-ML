import numpy as np


# Step 1
def kernel_function(x1: np.ndarray, x2: np.ndarray) -> int:
    # # Normal approach
    # dot_sum = 0
    # for i in range(len(x1)):
    #     dot_sum += x1[i] * x2[i]
    # return dot_sum

    # List comprehension of above
    dot_sum = 0
    dot_sum = [x1[i] * x2[i] for i in range(len(x1))]
    return sum(dot_sum)


# # Step 2
# def kernel_function(x1, x2):
#     # Your code here
#     return np.dot(x1, x2)

# # Step 3:
# def kernel_function(x1, x2):
#     # Your code here
#     return np.inner(x1, x2)


x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
# x1 = np.array([[1,2], [3,4]])
# x2 = np.array([[11,12], [13,14]])

result = kernel_function(x1, x2)
print(result)
