import numpy as np

def nesterov_momentum_step(w: list, v: list, grad: list, lr: float = 0.01, momentum: float = 0.9) -> dict:
    """
    Returns a dictionary with new_w and new_v.
    """
    # Write code here
    v_ts = []
    for (v_t_1, g_t) in zip(v, grad):
        v_ts.append(momentum*v_t_1 + lr*g_t) 

    w_ts = []
    for vt, w_t_1 in zip(v_ts, w):
        w_ts.append(w_t_1 - vt)

    return {"new_w": np.array(w_ts), "new_v": np.array(v_ts)}