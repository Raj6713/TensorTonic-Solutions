import numpy as np

def dcg(relevance_scores, k):
    relevance_scores = np.asarray(relevance_scores)[:k]
    scores = [
        (2**rel - 1) / np.log2(i + 2)   # i starts from 0 → position = i+1
        for i, rel in enumerate(relevance_scores)
    ]
    return np.sum(scores)

def ndcg(relevance_scores, k):
    dcg_val = dcg(relevance_scores, k)
    
    # Ideal DCG (sorted relevance)
    ideal_scores = sorted(relevance_scores, reverse=True)
    idcg_val = dcg(ideal_scores, k)
    
    if idcg_val == 0:
        return 0.0
    
    return dcg_val / idcg_val