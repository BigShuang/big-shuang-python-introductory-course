base = 100
rise_rate = 0.25
s = 0
for i in range(8):
    v = base*(1+rise_rate) ** i
    v = round(v)
    s += v
    print("index: %s, current price: %s, day income: %s" % (i+1, v, s))
