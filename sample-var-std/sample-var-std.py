import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    mean = sum(x)/n
    var = sum([float(i-mean)**2 for i in x]) / (n-1)
    std = float(np.sqrt(var))
    return {"variance": var, "standard_deviation": std}
    