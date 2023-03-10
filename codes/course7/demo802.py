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
        self.base_hp = self.hp  # base_hp: 当前等级总HP， 升级时是这个翻倍
        self.exp = [0, 20]  # 第一个是现有经验，第二个是升级需要的总经验。

    def show_info(self):
        """
        展示玩家信息。
        效果示例如下：
        ======= Player status ========
        HP: 20 / 200
        Attack: 20
        Defence: 20
        Lv: 2. EXP: 20/ 40
        ==============================
        """
        print("{:=^30s}".format(" Player status "))
        print("HP: %s / %s" % (self.hp, self.base_hp))
        print("Attack: %s" % self.attack)
        print("Defence: %s" % self.attack)
        print("Lv: %s. EXP: %s / %s" % (self.lv, self.exp[0], self.exp[1]))
        print("=" * 30)

    def win(self, enemy):
        exp = enemy.drop_exp()
        self.exp[0] += enemy.drop_exp()
        print("Defeat enemy: %s. Gain exp: %s. Current exp: %s / %s. Left hp: %s" %
              (enemy.__class__.__name__, exp, self.exp[0], self.exp[1] ,self.hp))

        if self.exp[0] >= self.exp[1]:
            self.exp[0] -= self.exp[1]  # 升级时扣除升级需要的经验
            self.lv_up()

    def lv_up(self):
        self.exp[1] = self.exp[1] * 2  # 每升一级，升级时需要的经验翻倍
        self.lv += 1

        # 每升一级，三维翻倍
        self.base_hp = self.base_hp * 2
        self.attack = self.attack * 2
        self.defence = self.defence * 2

        # 升级后，恢复满血
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
    def __init__(self):
        super().__init__(base=2)
    
    def hit(self, other):
        damage = self.attack
        if damage > 0:
            other.hp -= damage


class Boss(Enemy):
    def __init__(self):
        super().__init__(base=4)

    def hit(self, other):
        damage = self.attack
        if damage > 0:
            other.hp -= damage
            self.hp += damage


class Game:
    def __init__(self):
        self.player = Player()

    def run(self):
        print("Welcome to my game.")
        self.player.show_info()
        while True:
            cmd = input("Enter your command:")
            cmd = cmd.lower()
            if cmd == "s":
                self.player.show_info()
            elif cmd == "e":
                print("Bye")
                return
            else:
                self.handle_commands(cmd)

    def handle_commands(self, cmd):
        for c in cmd:
            if c == "e":
                enemy = Enemy()
            elif c == "a":
                enemy = AdvancedEnemy()
            elif c == "b":
                enemy = Boss()
            else:
                print("Invalid Input.")
                return

            self.fight(enemy)

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
game.run()