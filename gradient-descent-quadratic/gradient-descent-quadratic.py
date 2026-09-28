def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x = float(x0)
    grad_f = lambda x: 2*a*x + b
    for _ in range(steps):
        x = x - lr*grad_f(x)
    return x