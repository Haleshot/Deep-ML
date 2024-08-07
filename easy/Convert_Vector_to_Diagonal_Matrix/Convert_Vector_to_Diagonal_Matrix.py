import numpy as np

def make_diagonal(x : list[int | float]) -> list[list[int | float]]:
    l = [[0] * len(x)] * len(x)
    for i in range(len(x)):
        for j in  range(len(x)):
            if i == j:
                l[i][j] = (x[j])
                
    return l


x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)