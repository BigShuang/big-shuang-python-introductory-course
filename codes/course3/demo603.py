lst = ["range", "str", "continue", 12, True, "python", 3.14, "else"]

longest_index = -1
longest_length = -1

for i in range(len(lst)):
    item = lst[i]
    if isinstance(item, str):
        if len(item) > longest_length:
            longest_index = i
            longest_length = len(item)

if longest_index >= 0:
    print("Longest string: %s" % lst[longest_index] )
    print("Its' index: %s" % longest_index )
else:
    print("No string")
