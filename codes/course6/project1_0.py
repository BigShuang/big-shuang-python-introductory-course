WELCOME = "Welcome to light out flip game!"
ENTER  = "Select one lamp to light On/Off (Enter the index, start from 0): "
WIN = "Great!You light up all the lights"
INVALID = "Invalid input."


def get_lights(light_file):
    # 灯信息文本文件路径
    pass


def show_lights(lights):
    # 灯信息列表
    pass


def switch_light(lights, li):
    # lights为灯信息列表，li为要切换的灯的索引。
    pass


def check_all_on(lights):
    # 灯信息列表
    pass


def main(light_file):
    # 灯信息文本文件路径
    lights = get_lights(light_file)
    print(WELCOME)

    while True:
        show_lights(lights)

        if check_all_on(lights):
            break

        li = input(ENTER)
        if li.isdigit():
            li = int(li)
            if 0 <= li < len(lights):
                switch_light(lights, li)
                switch_light(lights, li - 1)
                switch_light(lights, li + 1)
                continue

        print(INVALID)

    print(WIN)

light_file = "lights.txt"
main(light_file)