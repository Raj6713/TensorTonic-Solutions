import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    output = []
    for item in vocab:
        counts = tokens.count(item)
        output.append(counts)
    return np.asarray(output, dtype=int)