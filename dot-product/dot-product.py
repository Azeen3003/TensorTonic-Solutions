import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    if len(x)==len(y):
        return np.sum(x*y)
    else:
        raise ValueError