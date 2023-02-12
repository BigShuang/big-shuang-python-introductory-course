s = "abcdcbcdacabac"
count_dict = {}

for c in s:
    if c not in count_dict:
        count_dict[c] = 1
    else:
        count_dict[c] += 1

print(count_dict)
