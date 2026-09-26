import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    single_feature = True if (not isinstance(X[0], list)) else False
    
    X_tf = []
    for row in X:
        row_l = [row] if not isinstance(row, list) else row
        X_tf.append([np.nan if l == "nan" else l for l in row_l])

    X_np = np.array(X_tf)
    # write the code considering the numpy array (2D) with np.nan is present

    n_dim, n_feats = X_np.shape
    mean = np.nan_to_num(np.nanmean(X_np, axis=0), nan=0)
    median = np.nan_to_num(np.nanmedian(X_np, axis=0), nan=0)

    for r in range(n_dim):
        for c in range(n_feats):
            if np.isnan(X_np[r,c]):
                X_np[r,c] = median[c] if strategy == 'median' else mean[c]

    #print(mean, median)
    print(X_np)
    if single_feature:
        X_np = np.squeeze(X_np, 1)
    return X_np
    