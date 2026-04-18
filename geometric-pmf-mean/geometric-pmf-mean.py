import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    
    k: int or array-like (k >= 1)
    p: probability of success (0 < p <= 1)
    
    Returns:
        pmf: same shape as k
        mean: scalar
    """
    k = np.asarray(k, dtype=float)
    
    if np.any(k < 1):
        raise ValueError("k must be >= 1 for geometric distribution")
    if not (0 < p <= 1):
        raise ValueError("p must be in (0, 1]")
    
    pmf = (1 - p) ** (k - 1) * p
    mean = 1 / p
    
    return pmf, mean