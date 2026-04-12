import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    diff = y_true-y_pred
    abs_diff = np.abs(diff)
    loss = np.where(abs_diff<=delta,
                   0.5*abs_diff*abs_diff,
                    delta*(abs_diff-0.5*delta)
                   )
    print(loss)
    return np.mean(loss)