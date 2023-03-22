class Blank:
    def __init__(self):
        pass

    def action(self, player):
        pass


class Fire(Blank): # hp - 10
    def action(self, player):
        player.change_hp(-10)


class Star(Blank): # hp + 10
    def action(self, player):
        player.change_hp(10)


class Player:
    def __init__(self, loc, hp=100):
        self.loc = loc
        self.hp = hp

    def move(self, grids):
        if self.loc + 1 < len(grids):
            self.loc += 1

    def change_hp(self, diff):
        self.hp += diff
        print("    Player hp change: %s. Current hp: %s" % (diff, self.hp))

    def show_info(self):
        print("Player current loc: %s, current hp: %s" % (self.loc, self.hp))


grid_map = {
    "_": Blank,
    "#": Fire,
    "*": Star,
}


class Game:
    def __init__(self, grid_line):
        self.player = Player(0, 100)
        self.grids = []

        for i in range(len(grid_line)):
            char = grid_line[i]
            gridClass = grid_map[char]
            grid = gridClass()
            self.grids.append(grid)

    def run(self):
        for i in range(len(self.grids)):
            cur_grid = self.grids[self.player.loc]
            self.player.show_info()
            cur_grid.action(self.player)
            if i < len(self.grids) -1: # 到最后一个格子之后不能再右移了
                self.player.move(self.grids)

        print("=== FINAL STATE ===")
        self.player.show_info()


grid_line1 = "_##_*_"
g1 = Game(grid_line1)
g1.run()