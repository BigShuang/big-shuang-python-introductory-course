lst = [8, 5, 7, 12, 19, 21, 10, 3, 2, 11]

min_index = 0
min_value = lst[min_index]
for i in range(1, len(lst)):
    if lst[i] < min_value:
        min_index = i
        min_value = lst[i]

print("Min Value: %s" % min_value )
print("Min Value's index: %s" % min_index )
