def dist(x, y):
    import math
    assert len(x) == len(y), 'Mismatch in shape'
    n_dim = len(x)
    dist = [0]*n_dim
    for d in range(n_dim):
        dist[d] += (x[d]-y[d])**2
    return math.sqrt(sum(dist))

def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    # pass
    assignments = []
    for pt in points:
        min_dist = float('inf')
        for i, centroid in enumerate(centroids):
            dist_centroid = dist(pt, centroid)
            if dist_centroid < min_dist:
                min_dist, min_dist_arg = dist_centroid, i
        assignments.append(min_dist_arg)    
    return assignments