# # Step 1
def leaky_relu(z: float, alpha: float = 0.01) -> float | int: # type: ignore
    # Your code here
    if z > 0:
        return z
    else:
        return alpha * z
