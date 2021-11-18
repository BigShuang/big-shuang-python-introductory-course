def get_no_repeat(lst):
    res = []
    for item in lst:
        if item not in res:
            res.append(item)

    return res


r = get_no_repeat([1,3,5,1,2])
print(r)
r = get_no_repeat([2,3,4,2,3,2,4])
print(r)
