import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    p = np.asarray(p)
    q = np.asarray(q)+eps
    kl_div = p*np.log(p/q)
    return np.sum(kl_div)