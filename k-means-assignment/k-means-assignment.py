import numpy as np
def k_means_assignment(points, centroids):
    points = np.asarray(points)
    centroids = np.asarray(centroids)
    
    # shape: (n_points, n_centroids)
    distances = np.linalg.norm(points[:, None, :] - centroids[None, :, :], axis=2)
    
    return np.argmin(distances, axis=1).tolist()