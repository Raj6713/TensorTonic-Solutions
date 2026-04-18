def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    values = np.asarray(values, dtype=float)
    values = values+1
    return np.log(values)