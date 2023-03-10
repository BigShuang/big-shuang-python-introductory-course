WELCOME = "Welcome to light out flip game!"
ENTER  = "Select one lamp to light On/Off (Enter the index, start from 0): "
WIN = "Great!You light up all the lights"

class LightsGame():
    def __init__(self, light_file):
        with open(light_file, 'r') as f:
            line = f.readline()

        self.lights = [item for item in line]

    def show(self):
        print("".join(self.lights))

    def switch_light(self, li):
        if 0 <= li < len(self.lights):
            if self.lights[li] == "-":
                self.lights[li] = "O"
            elif self.lights[li] == "O":
                self.lights[li] = "-"

    def check_all_on(self):
        for light in self.lights:
            if light == "-":
                return False

        return True

    def run(self):
        print(self.lights)

        print(WELCOME)
        while True:
            self.show()

            if self.check_all_on():
                print(WIN)
                return

            li = input(ENTER)

            if li.isdigit():
                li = int(li)
                if 0 <= li < len(self.lights):
                    self.switch_light(li)
                    self.switch_light(li - 1)
                    self.switch_light(li + 1)
                    continue

            print()


light_file = "lights.txt"
lg = LightsGame(light_file)
lg.run()