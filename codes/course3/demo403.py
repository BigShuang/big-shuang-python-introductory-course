lst = [8, 5, 7, 12, 19, 21, 10, 3, 2, 11]

max_index = 0
max_value = lst[max_index]
for i in range(1, len(lst)):
    if lst[i] > max_value:
        max_index = i
        max_value = lst[i]

print("Max Value: %s" % max_value)
print("Max Value's index: %s" % max_index)
