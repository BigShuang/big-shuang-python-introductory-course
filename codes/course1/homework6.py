s = 0
k = 1
for i in range(100):
    s += k / (i + 1)
    k = -k

print(s)
