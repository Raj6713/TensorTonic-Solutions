import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.asarray(X)
    x_min = np.min(X, axis=axis, keepdims=True)
    x_max = np.max(X, axis=axis, keepdims=True)
    print(X.shape, x_max.shape, x_min.shape)
    denom = x_max-x_min
    denom = np.maximum(denom, eps)
    X = (X-x_min)/denom
    return X
    