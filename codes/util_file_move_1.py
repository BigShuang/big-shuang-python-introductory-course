import os


def move(folder, start, step):
    imgs = os.path.listdir(folder)
    print(imgs)



if __name__ == '__main__':
    folder = "../imgs/0"
    start = (2, 11)
    step = 1
    move(folder, start, step)
