import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.asarray(x, dtype=float)
    mean = p
    variance = p*(1-p)
    output = np.pow(p,x)*np.pow(1-p, 1-x)
    return output, mean, variance
    
    pass