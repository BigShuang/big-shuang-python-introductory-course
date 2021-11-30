def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

prime_100 = [num for num in range(100) if is_prime(num)]
print(prime_100)
