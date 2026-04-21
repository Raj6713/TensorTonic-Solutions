import numpy as np
def hit_rate(recommendation, ground):
    value = set(recommendation).intersection(set(ground))
    if len(value)==0:
        return 0
    return 1

def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    recommendation_K = [item[:k] for item in recommendations]
    values = [hit_rate(item1,item2) for item1, item2 in zip(recommendation_K, ground_truth)]
    print(values)
    return np.mean(np.asarray(values, dtype=int))


    