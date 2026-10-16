def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    n_dim = len(points[0])
    coords = [[0]*n_dim for _ in range(k)]
    n_points = [0]*k

    for pt, cl in zip(points, assignments):
        n_points[cl] += 1
        for d in range(n_dim):
            coords[cl][d] += pt[d]
    
    for cl in range(k):
        if n_points[cl] != 0:
            for d in range(n_dim):
                coords[cl][d] /= n_points[cl]

    return coords