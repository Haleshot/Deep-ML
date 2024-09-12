# K-Means Clustering (Medium) ✔

## Table of Contents

- [Problem Statement](#problem-statement)
- [Example](#example)
- [Learn: Implementing k-Means Clustering](#learn-implementing-k-means-clustering)
- [Solutions](#solutions)
  - [Custom Implementation](#custom-implementation)
  - [NumPy Implementation](#numpy-implementation)
- [Code Explanation](#code-explanation)

## Problem Statement

[K-Means Clustering](https://www.deep-ml.com/problem/K-Means%20Clustering)

Write a Python function that implements the k-Means algorithm for clustering, starting with specified initial centroids and a set number of iterations. The function should take a list of points (each represented as a tuple of coordinates), an integer k representing the number of clusters to form, a list of initial centroids (each a tuple of coordinates), and an integer representing the maximum number of iterations to perform. The function will iteratively assign each point to the nearest centroid and update the centroids based on the assignments until the centroids do not change significantly, or the maximum number of iterations is reached. The function should return a list of the final centroids of the clusters. Round to the nearest fourth decimal.

## Example

```python
input: points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10
output: [(1, 2), (10, 2)]
reasoning: Given the initial centroids and a maximum of 10 iterations,
the points are clustered around these points, and the centroids are
updated to the mean of the assigned points, resulting in the final
centroids which approximate the means of the two clusters.
The exact number of iterations needed may vary,
but the process will stop after 10 iterations at most.
```

## Learn: Implementing k-Means Clustering

k-Means clustering is a method to partition $n$ points into $k$ clusters. Here is a brief overview of how to implement the k-Means algorithm:

1. **Initialization**: Start by selecting $k$ initial centroids. These can be randomly selected from the dataset or based on prior knowledge.

2. **Assignment Step**: For each point in the dataset, find the nearest centroid. The "nearest" can be defined using Euclidean distance. Assign the point to the cluster represented by this nearest centroid.

3. **Update Step**: Once all points are assigned to clusters, update the centroids by calculating the mean of all points in each cluster. This becomes the new centroid of the cluster.

4. **Iteration**: Repeat the assignment and update steps until the centroids no longer change significantly, or until a predetermined number of iterations have been completed. This iterative process helps in refining the clusters to minimize within-cluster variance.

5. **Result**: The final centroids represent the center of the clusters, and the points are partitioned accordingly.

This algorithm assumes that the mean is a meaningful measure, which might not be the case for non-numeric data. The choice of initial centroids can significantly affect the final clusters, hence multiple runs with different starting points can lead to a more comprehensive understanding of the cluster structure in the data.

## Solutions

### Custom Implementation

```python
import numpy as np
import math

def k_means_clustering(
    points: list[tuple[float, float]],
    k: int,
    initial_centroids: list[tuple[float, float]],
    max_iterations: int,
) -> list[tuple[float, float]]:
    def euc_dist(x1, x2):
        return math.sqrt(
            ((x2[1] - x1[1]) ** 2 + (x2[0] - x1[0]) ** 2)
        )  # Euclidean distance formula

    final_centroids = initial_centroids

    # Iterate for the given max_iterations
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]  # Create empty lists for clusters

        # Assign points to the nearest centroid (initial draft)
        for point in points:
            distance = [euc_dist(point, final_centroids[i]) for i in range(k)]
            closest_cluster_index = distance.index(min(distance))
            clusters[closest_cluster_index].append(point)

        new_centroids = []

        # Update centroids by computing the mean of points in each cluster
        for cluster in clusters:
            if cluster:  # Only update centroids if cluster is not empty
                new_centroid = tuple(np.round(np.mean(cluster, axis=0), 4))
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(
                    final_centroids[clusters.index(cluster)]
                )  # Keep the same centroid if no points in the cluster

        # If centroids do not change, break early
        if new_centroids == final_centroids:
            break
        final_centroids = new_centroids
    return final_centroids  # type: ignore

# Example usage
points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10
print(k_means_clustering(points=points, k=k, initial_centroids=initial_centroids, max_iterations=max_iterations))  # type: ignore
```

### NumPy Implementation

```python
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

# Example usage
points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 10
print(k_means_clustering(points=points, k=k, initial_centroids=initial_centroids, max_iterations=max_iterations))
```

## Code Explanation

### Custom Implementation

1. The `k_means_clustering` function takes four parameters: `points` (list of tuples), `k` (number of clusters), `initial_centroids` (list of tuples), and `max_iterations` (integer).

2. A helper function `euc_dist` is defined to calculate the Euclidean distance between two points.

3. The algorithm iterates for a maximum of `max_iterations` times:
   - It creates empty clusters for each centroid.
   - For each point, it calculates the distance to all centroids and assigns the point to the nearest centroid's cluster.
   - It then updates the centroids by calculating the mean of all points in each cluster.
   - If a cluster is empty, it keeps the previous centroid for that cluster.
   - If the new centroids are the same as the previous ones, it breaks the loop early.

4. The function returns the final centroids rounded to 4 decimal places.

5. The `# type: ignore` comments are used to suppress type checking warnings, likely due to potential type mismatches in the code.

### NumPy Implementation

1. The `euclidean_distance` function calculates the Euclidean distance between points using NumPy operations.

2. The `k_means_clustering` function is implemented using NumPy arrays for efficient computations:
   - It converts input points and centroids to NumPy arrays.
   - For each iteration, it calculates distances between all points and centroids using vectorized operations.
   - It assigns points to the nearest centroid using `np.argmin`.
   - New centroids are calculated as the mean of assigned points, or kept the same if a cluster is empty.
   - It checks for convergence by comparing new and old centroids.
   - Centroids are rounded to 4 decimal places.

3. The function returns the final centroids as a list of tuples.

Both implementations follow the same general algorithm but differ in their use of data structures and computational methods. The NumPy implementation is likely to be more efficient for larger datasets due to its use of vectorized operations.
