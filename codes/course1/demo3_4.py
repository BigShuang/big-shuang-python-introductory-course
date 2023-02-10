"""
题目：
某种物品时累进计费的（且限购八个），
买第1个的价格是100元。
之后每个，都在上一个的基础上涨价25%(结果四舍五入取整)。
即第2个的价格是125元。
第3个的价格是125(1+25%)=156
第4个的价格是156(1+25%)=195，
依此类推...

请展示依次购买时的：
购买个数(n)，对应单价(第n个的单价)，和总价
"""
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
