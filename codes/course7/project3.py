class Grid:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def action(self, player):
        print("Player currently in: r: %s, c: %s. " % (self.r, self.c))

class Blank(Grid):
    pass

class Fire(Grid): # hp - 10
    def action(self, player):
        super().action(player)
        player.change_hp(-10)

class Star(Grid): # hp + 10
    def action(self, player):
        super().action(player)
        player.change_hp(10)

grid_map = {
    "_": Blank,
    "#": Fire,
    "*": Star,
}

class Player:
    def __init__(self, hp=100):
        self.hp = hp

    def change_hp(self, diff):
        self.hp += diff
        print("Player hp change: %s. Current hp: %s" % (diff, self.hp))

class Game:
    def __init__(self, grid_line):
        self.player = Player(100)
        self.grids = []

        for i in range(len(grid_line)):
            char = grid_line[i]
            gridClass = grid_map[char]
            grid = gridClass(0, i)
            self.grids.append(grid)

    def run(self):
        for grid in self.grids:
            grid.action(self.player)

grid_line1 = "_##_*_"
g1 = Game(grid_line1)
g1.run()