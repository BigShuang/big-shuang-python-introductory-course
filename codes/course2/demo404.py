times_dict = {
    "A": 51,
    "B": 23,
    "C": 67,
    "D": 83,
    "E": 77,
}

directions = {
    0: "north",
    1: "west",
    2: "south",
    3: "east",
}

for name in times_dict:
    times = times_dict[name]
    circles = times // 4
    direction_index = times % 4

    direction = directions[direction_index]
    print('%s faces %s, turns %s circles.'%(name, direction, circles))
