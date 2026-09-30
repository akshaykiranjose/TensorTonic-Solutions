import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    # Write code here
    scores_np = np.array(scores)
    scores_masked_np = np.ma.array(scores_np, mask = np.triu(scores, k=1))
    scores_filled_np = scores_masked_np.filled(fill_value=mask_value)
    return scores_filled_np