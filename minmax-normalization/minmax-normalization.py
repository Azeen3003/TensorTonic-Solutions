import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.array(X, dtype=np.float64, copy=True)

    if X.ndim == 1:
        max = np.maximum(X)
        min = np.minimum(X)
        denominator = np.maximum((max-min), eps)
        min_max = (X-min)/denominator
    else:
        max = np.max(X, axis=axis, keepdims=True)
        min = np.min(X, axis=axis, keepdims=True)
        denominator = np.maximum((max-min), eps) 
        min_max = (X-min)/denominator

    return np.asarray(min_max, dtype=np.float64)