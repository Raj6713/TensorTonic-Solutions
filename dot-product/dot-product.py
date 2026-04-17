import numpy as np
import torch

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # x = torch.as_tensor(x, dtype=torch.float32)
    # y = torch.as_tensor(y, dtype=torch.float32)
    # return torch.dot(x,y).item()
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return np.dot(x,y)
    pass