def map_longest(words):
    if not words:
        return 0
    return max([len(word) for word in words])
