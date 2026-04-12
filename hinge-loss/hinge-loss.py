import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    scores = y_true*y_score
    scores = margin-scores
    scores = np.maximum(0, scores)
    if reduction == "mean":
        return np.mean(scores)
    elif reduction == "sum":
        return np.sum(scores)
    return scores