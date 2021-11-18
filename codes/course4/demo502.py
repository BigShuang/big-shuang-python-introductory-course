def get_max(lst):
    max_v = lst[0]
    for item in lst:
        if item > max_v:
            max_v = item

    return max_v

def get_min(lst):
    min_v = lst[0]
    for item in lst:
        if item < min_v:
            min_v = item

    return min_v

def cal_max_diff(lst):
    max_v = get_max(lst)
    min_v = get_min(lst)
    max_diff = max_v - min_v
    return max_diff


arr1 = [13, 15, 12, 19, 5, 7, 10]
print(cal_max_diff(arr1))
