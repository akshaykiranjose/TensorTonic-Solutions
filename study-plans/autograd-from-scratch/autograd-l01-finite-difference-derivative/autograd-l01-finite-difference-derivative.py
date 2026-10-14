import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    f = lambda x: sum(float(c_k * x**k) for k, c_k in enumerate(coefficients))
    f_x, f_x_plus_h = f(x), f(x+h)
    f_prime_x = (f_x_plus_h - f_x) / h
    return (f_x, f_x_plus_h, f_prime_x)