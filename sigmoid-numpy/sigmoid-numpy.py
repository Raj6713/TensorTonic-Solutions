import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)
    x = 1+np.exp(-x)
    return 1/x