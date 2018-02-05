def find_nearest_repetition(paragraph):
    """
    Idea : keep a dict dict[word] = lastIndex seen
    :param paragraph:
    :return:
    """
    shortest_distance = float("inf")
    last_index_word = {}
    for i, word in enumerate(paragraph) :
        if word in last_index_word :
            shortest_distance = min(i-last_index_word[word], shortest_distance)
            last_index_word[word] = i
    return shortest_distance