import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x)
    y= np.asarray(p)
    if not np.allclose(np.sum(p),1.0):
        raise ValueError()
    return np.sum(x*p)
