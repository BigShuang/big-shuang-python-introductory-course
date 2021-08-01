base = 100
rise_rate = 0.25
total_price = 0

for i in range(8):
    rate = (1 + rise_rate) ** i
    current_price = base * rate
    current_price = round(current_price)
    total_price += current_price

    line = "number: %s, current price: %s, total price: %s"
    print(line % (i+1, current_price, total_price))
