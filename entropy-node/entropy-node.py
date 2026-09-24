import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    #pass
    if not y:
        return 0.0
    N = len(y)
    unique_classes = np.unique(y)
    entropy = 0.0
    for cls in unique_classes:
        num_elements = np.where(y==cls, 1, 0).sum()
        if num_elements > 0:
            p_cls = num_elements / N
            entropy -= p_cls * np.log2(p_cls)

    return entropy
        

    