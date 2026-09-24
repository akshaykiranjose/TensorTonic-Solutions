import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.empty((0, 0)).astype(int)
    if not max_len:
        max_len = max((len(seq) for seq in seqs))

    padded_seq = []
    for seq in seqs:
        l = len(seq)
        if l > max_len:
            padded_seq.append(seq[:max_len])
        else:
            padded_seq.append(seq + [pad_value] * (max_len - l))

    return np.asarray(padded_seq)