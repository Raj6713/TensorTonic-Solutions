def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)
    tokens = [item for item in tokens if item not in stopwords]
    return tokens