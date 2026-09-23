import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    N, D = X.shape
    w, b = np.zeros(D), 0.0

    for iter in range(steps):

        P = _sigmoid(z = X@w + b)
        
        dL_by_dw = np.zeros(D)
        for j in range(D):
            for i in range(N):
                dL_by_dw[j] += X[i][j]*(P[i] - y[i])/N

            w[j] -= lr * dL_by_dw[j]

        dL_by_db = 0.
        for i in range(N):
            dL_by_db += (P[i] - y[i])/N

        b -= lr * dL_by_db

    return (w, b)
                
        
    
            