import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.asarray(X, dtype=float)
    X_min = np.min(X, axis=axis,keepdims=True)
    X_max = np.max(X, axis=axis,keepdims=True)
    print(X_min, X_max)
    denom = X_max-X_min
    denom = np.where(denom<eps,1.0,denom)
    X_scaled = (X - X_min)/denom
    return X_scaled
    pass