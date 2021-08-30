times = 51
circles = times // 4
direction_index = times % 4
direction = ""

if direction_index == 0:
    direction = "north"
if direction_index == 1:
    direction = "west"
if direction_index == 2:
    direction = "south"
if direction_index == 3:
    direction = "east"

print('Xiao Ming faces %s, turns %s circles.'%(direction, circles))
