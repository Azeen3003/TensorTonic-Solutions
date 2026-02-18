def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords_set = set(stopwords)
    return [element for element in tokens if element not in stopwords_set]