class Blank:
    def __init__(self):
        pass

    def action(self, player):
        pass


class Fire(Blank): # hp - 10
    def action(self, player):
        pass


class Star(Blank): # hp + 10
    def action(self, player):
        pass


class Player:
    def __init__(self, loc, hp=100):
        pass

    def move(self, grids):
        pass

    def change_hp(self, diff):
        pass

    def show_info(self):
        pass


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