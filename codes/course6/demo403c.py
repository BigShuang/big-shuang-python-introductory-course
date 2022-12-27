arr = [1, 3, 5, -1, 2, 4, -3, -2, 7]
arr2 = []
for i in range(len(arr)):
    if arr[i] < 0:
        arr2.append(i)

# for i in arr2[::-1]:  # slice [start: end: step]
for index in range(len(arr2)-1, -1, -1):  # range(start, end, step)
    i = arr2[index] # arr2 value
    r = arr.pop(i)
    print(i, r)

print(arr)