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


class Poison(Blank): # hp -10 * 3
    def action(self, player):
        player.set_status('poison', 3)


class Protect(Blank): # 未来2步 免疫任何伤害
    def action(self, player):
        player.set_status('protect', 3)


class Player:
    def __init__(self, loc, hp=100):
        self.loc = loc
        self.hp = hp
        self.status = {
            "protect": 0,
            "poison": 0
        }

    def set_status(self, status, steps):
        if status == "protect":
            if self.status["poison"] > 0:
                print("    Protected. Clear Poison")
                self.status["poison"] = 0
            self.status["protect"] = steps
        elif status == "poison":
            if self.status["protect"] > 0:
                print("    Protected. Poison Invalid.")
            else:
                self.status["poison"] = steps

    def update_status(self):
        poison_steps = self.status.get("poison", 0)
        protect_steps = self.status.get("protect", 0)
        if poison_steps > 0:
            print("    Decrease HP due to poisoning")
            self.change_hp(-10)
            self.status["poison"] -= 1

        if protect_steps > 0:
            self.status["protect"] -= 1

    def move(self, grids):
        if self.loc + 1 < len(grids):
            self.loc += 1

    def change_hp(self, diff):
        if diff < 0 and self.status.get("protect") > 0:
            print("    Protected. Decease hp Invalid.")
            return

        self.hp += diff
        print("    Player hp change: %s. Current hp: %s" % (diff, self.hp))

    def show_info(self):
        s = "Player current loc: %s, current hp: %s. " % (self.loc, self.hp)
        for key in self.status:
            if self.status[key] > 0:
                s += "Status: %s(%s) . " % (key, self.status[key])

        print(s)


grid_map = {
    "_": Blank,
    "#": Fire,
    "*": Star,
    "!": Poison,
    "+": Protect
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
            self.player.update_status()
            if i < len(self.grids) -1: # 到最后一个格子之后不能再右移了
                self.player.move(self.grids)

        print("=== FINAL STATE ===")
        self.player.show_info()


grid_line1 = "_!+_#__"
g1 = Game(grid_line1)
g1.run()

print()

grid_line2 = "_+###_"
g2 = Game(grid_line2)
g2.run()

print()

grid_line3 = "_+!#__"
g3 = Game(grid_line3)
g3.run()
