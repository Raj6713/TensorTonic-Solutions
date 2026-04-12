import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    print(x1, x2, label, margin)
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    cosine_similarity = compute_cosine(x1, x2)
    if label == 1:
        loss = 1-cosine_similarity
    elif label == -1:
        loss = max(0, cosine_similarity-margin)
    return loss

    
def compute_cosine(x1, x2):
    return np.sum(x1*x2)/(np.linalg.norm(x1)*np.linalg.norm(x2))
    