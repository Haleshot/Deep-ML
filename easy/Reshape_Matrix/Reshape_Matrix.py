import numpy as np

# # Step 1:
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    l = [[0] * new_shape[1] for _ in range(new_shape[0])]
    print(l)
    for i in range(new_shape[1]):
        for j in range(new_shape[0]):
            l[i][j] = a[i][j] # type: ignore
            print(l)
            
        l = [i for i in l if i not in a]
    # l = [a[j][i] for j in range(new_shape[0]) for i in range(new_shape[1])]

    return l # type: ignore

# # Step 2
# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
#     # Write your code here and return a python list after reshaping by using numpy's tolist() method
#     return np.reshape(a, newshape=new_shape).tolist()

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
print(reshape_matrix(a=a, new_shape=new_shape)) # type: ignore