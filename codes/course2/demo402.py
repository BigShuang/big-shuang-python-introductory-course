times = 51
circles = times // 4
direction_index = times % 4
directions = {
    0: "north",
    1: "west",
    2: "south",
    3: "east",
}

direction = directions[direction_index]
print('Xiao Ming faces %s, turns %s circles.'%(direction, circles))
