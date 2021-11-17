def calculate_sum(n):
    k = 1
    s = 0
    for i in range(n):
        s += k / (i + 1)
        k = -k
    print("n=%s: S=%s" % (n, s))

calculate_sum(100)
calculate_sum(1000)
calculate_sum(10000)
calculate_sum(100000)
