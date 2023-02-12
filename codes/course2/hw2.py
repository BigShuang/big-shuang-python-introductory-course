infos = [
    "Alan, 19",
    "Bruce, 22",
    "Carlos, 23",
    "David, 18",
    "Emma, 21"
]

for info in infos:
    name, age = info.split(",")
    age = age.strip()
    print("I am %s. I'm %s years old." % (name, age))
