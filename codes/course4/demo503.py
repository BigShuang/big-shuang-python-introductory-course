def check_all_match_size(words, size):
    for word in words:
        if len(word) != size:
            return False

    return True
