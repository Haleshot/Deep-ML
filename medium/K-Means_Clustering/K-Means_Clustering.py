import numpy as np
import math
def k_means_clustering(
    points: list[tuple[float, float]],
    k: int,
    initial_centroids: list[tuple[float, float]],
    max_iterations: int,
) -> list[tuple[float, float]]:
    # Your code here
    def euc_dist(x1, x2):
        return math.sqrt((x2[0] - x1[0])**2 - (x2[1] - x2[1])**2)
    for _ in range(max_iterations):
        pass

    return final_centroids  # type: ignore


points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10
