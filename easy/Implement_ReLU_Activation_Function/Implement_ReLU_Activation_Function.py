# # Step 1:
def relu(z: float) -> float:
    return max(0, z)


# # Step 2
# def relu(z: float) -> float:
#     # Your code here
#     if z <= 0:
#         return 0
#     else:
#         return max(0, z)


# Testing
print(relu(2))
