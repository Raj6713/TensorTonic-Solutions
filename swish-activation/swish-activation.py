import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x)
    x_ = np.exp(-x)
    return x*(1/(1+x_))