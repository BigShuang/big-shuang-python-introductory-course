names = ["A", "B", "C", "D", "E"]
times_list = [51, 23, 67, 83, 77]

directions = ["north", "west", "south", "east"]

for i in range(len(names)):
    name = names[i]
    times = times_list[i]
    circles = times // 4
    direction_index = times % 4

    direction = directions[direction_index]
    print('%s faces %s, turns %s circles.'%(name, direction, circles))
