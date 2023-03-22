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


class Game:
    def __init__(self, grid_line):
        pass

    def run(self):
        pass


grid_line1 = "_##_*_"
g1 = Game(grid_line1)
g1.run()