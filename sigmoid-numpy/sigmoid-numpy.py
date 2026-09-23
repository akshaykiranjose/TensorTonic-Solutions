import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x_np = np.asarray(x)
    x_exp = np.exp(-x_np)
    x_sigmoid = 1 / (1 + x_exp)
    return x_sigmoid