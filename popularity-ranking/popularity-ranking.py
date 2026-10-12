def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    # pass
    weighted_ratings = []
    for (avg_rating, vote_count) in items:
        rating_w = vote_count / (vote_count + min_votes)
        weighted_ratings.append(rating_w*avg_rating + (1-rating_w)*global_mean)
    return weighted_ratings