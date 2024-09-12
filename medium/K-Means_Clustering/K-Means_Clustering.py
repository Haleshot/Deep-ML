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
        return math.sqrt(
            ((x2[1] - x1[1]) ** 2 + (x2[0] - x1[0]) ** 2)
        )  # Euclidean distance formula

    final_centroids = initial_centroids
    # print(final_centroids)
    update_centroids = []
    # for _ in range(max_iterations):
    for point in points:
        dist_metric1 = euc_dist(point, initial_centroids[0])
        dist_metric2 = euc_dist(point, initial_centroids[1])
        cluster = min(dist_metric1, dist_metric2)
        update_centroids.append([point, cluster])
    # # list_clusters = [1, 2, 3, 4]
    # # filtered = filter(lambda key: key[1] == [i for i in list_clusters], update_centroids)
    # # print(list(filtered))
    # filtered = list[tuple[float, float]]
    # for centroid in update_centroids:
    #     if centroid[1] == 1:
    #         filtered.append()
    update_centroids = sorted(update_centroids, key=lambda x:x[1])
    update_centroids = np.sum(update_centroids, axis=1)
    sum(update_centroids, )

    return update_centroids  # type: ignore


points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10
print(k_means_clustering(points=points, k=k, initial_centroids=initial_centroids, max_iterations=max_iterations))  # type: ignore
