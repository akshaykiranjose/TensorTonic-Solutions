import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    Row = len(A)
    Col = len(A[0]) #if isinstance(A[0], list) else 1

    Output = []
    for c in range(Col):
        Output.append([row[c] for row in A])

    return np.array(Output)
