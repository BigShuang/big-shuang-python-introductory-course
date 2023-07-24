lst = [8, 5, 7, -12, 19, 21, 10, -3, 2, 11]
weights = [1, 2, 5, 3, 4, 6, 8, 7, 2, 4]

s = 0
for i in range(len(lst)):
    item = lst[i]
    if item < 0:
        continue

    weight = weights[i]
    v = item * weight
    s += v

print(s)
