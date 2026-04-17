import numpy as np
import torch

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = torch.as_tensor(a, dtype=torch.float32)
    b = torch.as_tensor(b, dtype=torch.float32)
    norm_a = torch.linalg.norm(a)
    norm_b = torch.linalg.norm(b)
    if norm_a.item() == 0 or norm_b.item() == 0:
        return 0
    return (torch.dot(a, b)/(norm_a*norm_b)).item()
    # a = np.asarray(a,dtype=float)
    # b = np.asarray(b, dtype=float)
    # norm_a = np.linalg.norm(a)
    # norm_b = np.linalg.norm(b)
    # if norm_a == 0 or norm_b == 0:
    #     return 0
    # return np.dot(a, b)/(norm_a*norm_b)