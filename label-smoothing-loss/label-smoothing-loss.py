import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    # Write code here
    K = len(predictions)
    smoothed_targets = [epsilon/K] * K
    smoothed_targets[target] += (1-epsilon)
    return sum(-q_i*math.log(p_i) for (q_i, p_i) in zip(smoothed_targets, predictions))
    
    