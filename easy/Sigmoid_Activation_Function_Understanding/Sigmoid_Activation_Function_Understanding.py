import numpy as np

def sigmoid(z: float) -> float:
    # Your code here
    return round(1/(1 + np.exp(-z)), 4)

z = 0
print(sigmoid(z=z))