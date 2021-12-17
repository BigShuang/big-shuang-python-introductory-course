WELCOME = "Welcome to light out flip game!"
ENTER  = "Select one lamp to light On/Off (Enter the index, start from 0): "
WIN = "Great!You light up all the lights"
INVALID = "Invalid input."


def get_lights(light_file):
    with open(light_file, 'r') as f:
        line = f.readline()

    lights = [item for item in line]
    return lights


def show_light(lights):
    print("".join(lights))


def switch_light(lights, li):
    if 0 <= li < len(lights):
        if lights[li] == "-":
            lights[li] = "O"
        elif lights[li] == "O":
            lights[li] = "-"


def check_all_on(lights):
    for light in lights:
        if light == "-":
            return False

    return True


def main(light_file):
    lights = get_lights(light_file)

    print(WELCOME)
    while True:
        show_light(lights)

        if check_all_on(lights):
            print(WIN)
            return

        li = input(ENTER)

        if li.isdigit():
            li = int(li)
            if 0 <= li < len(lights):
                switch_light(lights, li)
                switch_light(lights, li-1)
                switch_light(lights, li+1)
                continue

        print(INVALID)


light_file = "lights.txt"
main(light_file)