def check_any_match_size(words, size):
    for word in words:
        if len(word) == size:
            return True

    return False


r = check_any_match_size(['lion', 'deer', 'bear'], 5)
print(r)
r = check_any_match_size(['lion', 'deer', 'sheep'], 5)
print(r)
