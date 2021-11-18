def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def show_all_prime(n):
    res = []
    for i in range(2, n):
        if is_prime(i):
            res.append(i)

    return res


r = show_all_prime(20)
print(r)
