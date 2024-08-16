import numpy as np


# Step 1:
def make_diagonal(x: list[int | float]) -> list[list[int | float]]:
    l = [[0] * len(x) for _ in range(len(x))]
    for i in range(len(x)):
        l[i][i] = x[i]  # type: ignore
    return np.array(l).tolist()


# # Step 2
# def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
#     return np.identity(np.size(x)) * x


x = np.array([1, 2, 3])
output = make_diagonal(x=x)  # type: ignore
print(output)
