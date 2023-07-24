lst = [8, 5, 7, 12, 19, 21, 10, 3, 2, 11]

mv = lst[0]
for item in lst:
    if item > mv:
        mv = item

print("Max Value: %s" % mv)