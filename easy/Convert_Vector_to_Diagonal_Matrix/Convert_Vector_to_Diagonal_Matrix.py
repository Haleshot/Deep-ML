import numpy as np

# # Step 1:
def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
    l = [[0] * len(x)] * len(x)
        # for i in range(len(x)):
        #     for j in  range(len(x)):
        #         if i == j:
        #             l[i][j] = x[i]
        #             print(l[i][j])
        #         l = [i for i in l if i not in ] 
    return l



# # Step 2
# def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
#     return np.identity(np.size(x)) * x


x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)