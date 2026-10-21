import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p_np, y_np = np.array(p).ravel(), np.array(y).ravel()
    return float(1 - (2*np.sum(p_np*y_np) + eps) / (p_np.sum() + y_np.sum() + eps))