import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    trace=0
    n = np.shape(A)[0]
    idx = np.arange(n)
    for idx in range(n):
        trace+= A[idx][idx]
    return trace
