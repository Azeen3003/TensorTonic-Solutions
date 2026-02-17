import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m, n = np.shape(A)
    transpose = np.zeros((n,m))
    for i in range(m):
        for j in range(n):
            transpose[j][i] =  A[i][j]
    return transpose
            
