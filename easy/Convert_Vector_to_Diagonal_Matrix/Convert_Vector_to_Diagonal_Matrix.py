import numpy as np

# # Step 1:
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    l = list(zip(*a))
    print(new_shape[0], "\t", new_shape[1])
    # for i in range(new_shape[1]):
    #     for j in range(new_shape[0]):
    #         print(j)
    # l = [a[j][i] for j in range(new_shape[0]) for i in range(new_shape[1])]
    return l

# # Step 2
# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
#     # Write your code here and return a python list after reshaping by using numpy's tolist() method
#     return np.reshape(a, newshape=new_shape).tolist()

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
print(reshape_matrix(a=a, new_shape=new_shape))