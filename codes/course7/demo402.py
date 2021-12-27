class Person:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def hit(self, other):
        damage = self.attack - other.defence
        if damage > 0:
            other.hp -= damage

    def is_alive(self):
        return self.hp > 0


class Player(Person):
    def __init__(self):
        hp, attack, defence = 100, 10, 5
        super().__init__(hp, attack, defence)

        self.lv = 1
        self.base_hp = self.hp
        self.exp = [0, 20]

    def win(self, enemy):
        exp = enemy.drop_exp()
        self.exp[0] += enemy.drop_exp()
        print("Defeat enemy: %s. Gain exp: %s. Current exp: %s / %s. Left hp: %s" %
              (enemy.__class__.__name__, exp, self.exp[0], self.exp[1] ,self.hp))

        if self.exp[0] >= self.exp[1]:
            self.exp[0] -= self.exp[1]
            self.lv_up()

    def lv_up(self):
        self.exp[1] = self.exp[1] * 2
        self.lv += 1

        self.base_hp = self.base_hp * 2
        self.attack = self.attack * 2
        self.defence = self.defence * 2

        self.hp = self.base_hp
        print("You upgraded, current level: %s, current hp: %s." % (self.lv, self.hp))

    def lose(self, enemy):
        print("You lost. %s's left hp: %s" % (enemy.__class__.__name__, enemy.hp))



class Enemy(Person):
    def __init__(self, base=1):
        hp, attack, defence = 50 * base, 10 * base, 5 * base
        super().__init__(hp, attack, defence)

        self.exp = 10 * base

    def drop_exp(self):
        return self.exp


class AdvancedEnemy(Enemy):
    def hit(self, other):
        damage = self.attack
        if damage > 0:
            other.hp -= damage

    def drop_exp(self):
        return self.exp * 2


class Boss(Enemy):
    def hit(self, other):
        damage = self.attack
        if damage > 0:
            other.hp -= damage
            self.hp += damage

    def drop_exp(self):
        return self.exp * 3


item_map = {
    "e": Enemy,
    "a": AdvancedEnemy,
    "b": Boss,
}


class Game:
    def __init__(self):
        self.player = Player()
        self.running = True

    def run(self):
        while self.running:
            cmd = input("Enter your command:")
            cmd = cmd.lower()
            if cmd == "s":
                pass
            else:
                self.handle_commands(cmd)

    def handle_commands(self, cmd):
        for c in cmd:
            item_class = item_map[c]
            item = item_class()
            if isinstance(item, Enemy):
                self.fight(item)

    def fight(self, enemy):
        while True:
            self.player.hit(enemy)
            if not enemy.is_alive():
                self.player.win(enemy)
                return

            enemy.hit(self.player)
            if not self.player.is_alive():
                self.player.lose(enemy)
                exit()


game = Game()
game.handle_commands("eeab")