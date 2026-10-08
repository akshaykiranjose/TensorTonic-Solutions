def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    # Write code here
    num_values = len(values)
    num_weights = len(weights)
    sum_weights = sum(weights) 
    WMA = []
    for i in range(num_values - num_weights + 1):
        wma = sum([w*x for (w,x) in zip(weights, values[i:])]) / sum_weights
        WMA.append(wma)
    return WMA
    