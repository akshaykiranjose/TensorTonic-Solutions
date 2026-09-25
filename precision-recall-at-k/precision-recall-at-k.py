def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    # recommended contains at-least K
    # relevant contains at-least 1

    top_k = recommended[:k]
    precision_k = len(set.intersection(set(top_k), set(relevant)))/len(top_k)
    recall_k = len(set.intersection(set(top_k), set(relevant)))/len(relevant)
    return [precision_k, recall_k]
    