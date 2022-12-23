
def increase_count():
    global count
    count += 1


def decrease_count():
    global count
    count -= 1


def main():
    global count
    count = 10

    while True:
        print("COUNT NUM: %s" % count)
        s = input("input: ")
        for c in s:
            if c == "w":
                increase_count()
            elif c == "s":
                decrease_count()
            elif c == "e":
                print("BYE")
                return

main()