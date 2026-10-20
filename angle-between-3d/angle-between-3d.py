import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    v_np, w_np = np.array(v), np.array(w)
    cosine = np.dot(v_np, w_np) / np.sqrt(np.dot(v_np, v_np) * np.dot(w_np, w_np))
    return np.arccos(cosine)