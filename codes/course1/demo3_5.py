n = 100
k = 1
s = 0
for i in range(n):
    s += k / (i + 1)
    k = -k
print("n=%s: S=%s" % (n, s))


n = 1000
k = 1
s = 0
for i in range(n):
    s += k / (i + 1)
    k = -k
print("n=%s: S=%s" % (n, s))


n = 10000
k = 1
s = 0
for i in range(n):
    s += k / (i + 1)
    k = -k
print("n=%s: S=%s" % (n, s))
