names = ["Alan", "Bruce", "Carlos", "David", "Emma"]

scores = [90, 80, 85, 92, 81]

info_list = [
    ("Alan", 90),
    ("Bruce", 80),
    ("Carlos", 85),
    ("David", 92),
    ("Emma", 81),
]


info_dict = {
    'Alan': 90,
    'Bruce': 80,
    'Carlos': 85,
    'David': 92,
    'Emma': 81
}

for name in info_dict:
    score = info_dict[name]
    print("%s, your's math score is %s." % (name, score))
