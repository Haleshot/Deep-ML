import math
import numpy as np

# # Step 1


def sigmoid(z):
    return round(1 / (1 + math.exp(-z)), 4)


# # Step 2
# def sigmoid(z: float) -> float:
#     # Your code here
#     return round(1 / (1 + np.exp(-z)), 4)


z = 0
print(sigmoid(z=z))
