import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    # pass
    return float(1 / len(fake_scores) * np.sum(fake_scores) - 1 / len(real_scores) * np.sum(real_scores))