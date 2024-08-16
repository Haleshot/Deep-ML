# # Step 1:
def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    l = [[0] * new_shape[1] for _ in range(new_shape[0])]
    flat_a = [elem for row in a for elem in row]  # Flatten the original matrix
    # print(flat_a)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            l[i][j] = flat_a[i * new_shape[1] + j]  # type: ignore
    return l  # type: ignore


# # Step 2
# import numpy as np
# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
#     # Write your code here and return a python list after reshaping by using numpy's tolist() method
#     return np.reshape(a, newshape=new_shape).tolist()

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
print(reshape_matrix(a=a, new_shape=new_shape))  # type: ignore
