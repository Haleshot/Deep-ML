import numpy as np
import math

# # Step 1
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
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in points:
            distance = [euc_dist(point, final_centroids[i]) for i in range(k)]
            closest_cluster_index = distance.index(min(distance))
            clusters[closest_cluster_index].append(point)
        # print(clusters)
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroid = tuple(np.round(np.mean(cluster, axis=0), 4))
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(final_centroids[clusters.index(cluster)])
        if new_centroids == final_centroids:
            break
        final_centroids = new_centroids

    # sum = 0
    # for i in update_centroids:
    #     sum += np.sum(i[0])
    # print(sum)

    return final_centroids # type: ignore

# # Step 2
import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(((a - b) ** 2).sum(axis=1))

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points)
    centroids = np.array(initial_centroids)
    
    for iteration in range(max_iterations):
        # Assign points to the nearest centroid
        distances = np.array([euclidean_distance(points, centroid) for centroid in centroids])
        assignments = np.argmin(distances, axis=0)

        new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i] for i in range(k)])
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
        centroids = np.round(centroids,4)
    return [tuple(centroid) for centroid in centroids]


points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10
print(k_means_clustering(points=points, k=k, initial_centroids=initial_centroids, max_iterations=max_iterations))  # type: ignore
