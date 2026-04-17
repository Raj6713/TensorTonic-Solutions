import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    X = np.asarray(X,dtype=float)
    x_mean = np.mean(X,axis=axis, keepdims=True)
    x_std = np.std(X, axis=axis, keepdims=True)
    x_std = x_std + eps
    X = (X-x_mean)/x_std
    print(x_mean)
    print(x_std)
    return X