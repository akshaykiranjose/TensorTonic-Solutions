import numpy as np

def triplet_loss(anchor: list, positive: list, negative: list, margin: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    # pass
    # find the dimension
    D = len(anchor[0]) if isinstance(anchor[0], list) else len(anchor)
    N = len(anchor) if isinstance(anchor[0], list) else 1
    
    anchor_np = np.array(anchor).reshape(N, D)
    positive_np = np.array(positive).reshape(N, D)
    negative_np = np.array(negative).reshape(N, D)

    positve_dist = np.linalg.norm(anchor_np - positive_np, axis=-1)**2
    negative_dist = np.linalg.norm(anchor_np - negative_np, axis=-1)**2

    #print(positve_dist, negative_dist)
    
    L = np.maximum(0, positve_dist - negative_dist + margin)

    return L.mean(axis=0).item()