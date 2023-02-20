shop_cart = [
    ("apple", 20),
    ("banana", 20),
    ("cherry", 15),
    ("apple", 30),
    ("banana", 10),
    ("banana", 25),
]

shop_dict = {}
for item in shop_cart:
    name, weight = item
    if name not in shop_dict:
        shop_dict[name] = weight
    else:
        shop_dict[name] += weight

for name in shop_dict:
    weight = shop_dict[name]
    print("%s: %s"% (name, weight))
