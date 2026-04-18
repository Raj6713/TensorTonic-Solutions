def rank_transform(values):
    n = len(values)
    
    # Pair each value with its original index
    indexed = list(enumerate(values))  # [(idx, value), ...]
    
    # Sort by value
    indexed.sort(key=lambda x: x[1])
    
    ranks = [0.0] * n
    
    i = 0
    while i < n:
        j = i
        
        # Find range of equal values (ties)
        while j < n and indexed[j][1] == indexed[i][1]:
            j += 1
        
        # Average rank (1-based)
        avg_rank = (i + j - 1) / 2 + 1
        
        # Assign to all tied elements
        for k in range(i, j):
            original_idx = indexed[k][0]
            ranks[original_idx] = avg_rank
        
        i = j
    
    return ranks