def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    # pass
    w_t = 1
    W = []
    for r_t in returns:
        w_t_minus_1 = w_t
        w_t = w_t_minus_1*(1+r_t)
        W.append(w_t)

    return [w_t-1 for w_t in W]