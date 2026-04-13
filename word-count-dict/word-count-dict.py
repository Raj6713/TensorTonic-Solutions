def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    dictionary = {}
    for item in sentences:
        for it in item:
            if it not in dictionary.keys():
                dictionary[it]=1
            else:
                dictionary[it]+=1
    return dictionary