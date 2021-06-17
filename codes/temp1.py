
def show_odd(n):
    print("n:", n)
    for i in range(n):
        print(i)
        if i % 2 == 0:
            print("Odd number:",i)


n = 10
show_odd(n)
