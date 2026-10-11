import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    # pass
    N = len(y)
    rng = np.random.default_rng(seed)
    permute_idx = rng.permutation(np.arange(N))
    if drop_last:
        N = N-N%batch_size
    X = np.array(X)[permute_idx[:N]]
    y = np.array(y)[permute_idx[:N]]
    for i in range(0, N, batch_size):
        yield (X[i: i+batch_size], y[i: i+batch_size])