def calculate_sum(n):  # n: parameter，形参，formal parameter
    k = 1
    s = 0
    for i in range(n):
        s += k / (i + 1)
        k = -k
    print("n=%s: S=%s" % (n, s))

a = 100
calculate_sum(a)  # a: argument，实参，actual argument
