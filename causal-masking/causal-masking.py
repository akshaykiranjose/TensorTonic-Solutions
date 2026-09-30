import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    # Write code here
    scores_np = np.array(scores)
    T = scores_np.shape[-1]
    mask = np.triu(np.ones((T,T), dtype=bool), k=1)
    scores_filled = scores.copy()
    scores_filled[..., mask] = mask_value
    return scores_filled