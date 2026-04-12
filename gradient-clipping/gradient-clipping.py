import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    if max_norm<=0:
        return np.asarray(g)
    g = np.asarray(g)
    norm_g = np.linalg.norm(g)
    if norm_g > max_norm and norm_g >0:
        g = g*(max_norm/norm_g)
    return g