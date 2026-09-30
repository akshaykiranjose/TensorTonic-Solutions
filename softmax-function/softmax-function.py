import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x_np = np.array(x)
    x_np = x_np - np.max(x_np, axis=-1, keepdims=True)
    x_exp_np = np.exp(x_np)
    x_exp_sum_np = np.sum(x_exp_np, axis=-1, keepdims=True)
    x_softmax = x_exp_np / x_exp_sum_np
    return x_softmax
    