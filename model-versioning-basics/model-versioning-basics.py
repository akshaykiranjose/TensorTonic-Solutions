def promote_model(models: list) -> str:
    """
    Returns the model name as a string.
    """
    # Write code here
    
    # if there are multiple models overall
    sorted_acc_models = sorted(models, key = lambda m: m['accuracy'], reverse = True) #highest first
    best_acc = sorted_acc_models[0]['accuracy']

    only_best_sorted_acc_models = list(filter(lambda m: m['accuracy'] == best_acc, sorted_acc_models))
    if len(only_best_sorted_acc_models) == 1:
        return only_best_sorted_acc_models[0]['name']

    # if there are multiple with the same accuracy

    sorted_lat_models = sorted(only_best_sorted_acc_models, key = lambda m: m['latency']) #lowest first
    best_lat = sorted_lat_models[0]['latency']
    only_best_sorted_lat_models = list(filter(lambda m: m['latency'] == best_lat, sorted_lat_models))
    if len(only_best_sorted_lat_models) == 1:
        return only_best_sorted_lat_models[0]['name']

    # if there are multiple with the same accuracy and latency

    sorted_time_models = sorted(only_best_sorted_lat_models, key = lambda m: m['timestamp'], reverse = True) #latest first
    best_time = sorted_time_models[0]['timestamp']
    only_best_sorted_time_models = list(filter(lambda m: m['timestamp'] == best_time, sorted_time_models))
    if len(only_best_sorted_time_models) == 1:
        return only_best_sorted_time_models[0]['name']
    else:
        raise ValueError('Multiple models with same accuracy, latency and timestamp')


    


    