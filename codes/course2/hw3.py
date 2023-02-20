info_list = [
    ("Alan", 90),
    ("Bruce", 80),
    ("Carlos", 85),
    ("David", 92),
    ("Emma", 81),
]

info_dict = {}

for item in info_list:
    name, age = item
    info_dict[name] = age

print(info_dict)
