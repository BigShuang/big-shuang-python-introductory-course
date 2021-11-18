def get_linear_y(x, k=1, b=0):
    y = k * x + b
    return y


for x in range(0, 6):
    y1 = get_linear_y(x, 2, 1)
    y2 = get_linear_y(x, 1, 2)
    print("x = %s, y1 = %s, y2 = %s" % (x, y1, y2))
