import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_pred = [item[it] for item, it in zip(y_pred, y_true)]
    value = -np.mean(np.log(y_pred))
    return value