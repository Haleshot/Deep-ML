def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    covariance_matrix = [[] for _ in range(len(vectors))]
    for i in vectors:
        meanX = sum(i)/len(i)
        j = vectors[vectors.index(i) + 1]
        meanY = sum(j)/len(j)
        covariance_matrix += [meanX + meanY]
    covariance_matrix = covariance_matrix/len(vectors) - 1

    return covariance_matrix


vectors = [[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(vectors=vectors))  # type: ignore
