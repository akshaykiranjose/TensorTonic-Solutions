def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    """
    Returns the expression value and numerical partials for a, b, and c.
    """
    f = lambda a,b,c: float(a*b + c)

    f_abc = f(a, b, c)
    df_da = (f(a+h, b, c) - f_abc)/h
    df_db = (f(a, b+h, c) - f_abc)/h
    df_dc = (f(a, b, c+h) - f_abc)/h

    return (f_abc, df_da, df_db, df_dc)
