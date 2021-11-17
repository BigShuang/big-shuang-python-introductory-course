def get_sum(n):
    k = 1
    s = 0
    for i in range(n):
        s += k / (i + 1)
        k = -k

    return s

s0 = get_sum(10)
s1 = get_sum(100)
s2 = get_sum(1000)
s3 = get_sum(10000)

print("10->100    : %s" % (s1-s0))
print("100->1000  : %s" % (s2-s1))
print("1000->10000: %s" % (s3-s2))
