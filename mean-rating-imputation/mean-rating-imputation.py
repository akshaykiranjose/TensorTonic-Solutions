def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    """
    # Write code here
    # find a user-mean and item-mean before we start replacing any values

    n_users = len(ratings_matrix)
    n_items = len(ratings_matrix[0])

    imputed_ratings_matrix = [row[:] for row in ratings_matrix] 

    if mode == 'user':
        #compute the user_means list
        rated_items = [[i for i in row if i != 0] for row in ratings_matrix]
        
    if mode == 'item':
        rated_items = []
        for n_i in range(n_items):
            rated_items.append([row[n_i] for row in ratings_matrix if row[n_i] != 0])
    
    means_list = [sum(l)/len(l) if l else 0 for l in rated_items]

    for r in range(n_users):
            for c in range(n_items):
                if ratings_matrix[r][c] == 0:
                    imputed_ratings_matrix[r][c] = means_list[r if mode == 'user' else c]

    return imputed_ratings_matrix

        
        

    