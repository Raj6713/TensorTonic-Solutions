def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    item_k = recommended[:k]
    precision = len(set(item_k).intersection(set(relevant)))/k
    recall = len(set(item_k).intersection(set(relevant)))/len(set(relevant))
    return [precision, recall]