def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    # Write code here
    import math
    N = len(values)
    k = (N-1)*lower_pct / 100
    q_low= values[int(k)] + (k-int(k))*(values[math.ceil(k)] - values[int(k)])

    k = (N-1)*upper_pct / 100
    q_high= values[int(k)] + (k-int(k))*(values[math.ceil(k)] - values[int(k)])

    clipped_values = []
    for val in values:
        if val < q_low:
            clipped_values.append(q_low)
        elif val > q_high:
            clipped_values.append(q_high)
        else:
            clipped_values.append(val)

    return clipped_values