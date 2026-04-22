def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    overall_union = set()
    for item in recommendations:
        overall_union = overall_union.union(set(item))
    print(overall_union)
    return len(overall_union)/n_items