import os


def move(folder, start, step):
    imgs = os.listdir(folder)
    names = []
    ss = "%s_" % start[0]
    for img in imgs:
        if img.startswith(ss):
            name, suffix = os.path.splitext(img)
            ci, index = name.split("_")
            index = int(index)
            if index >= start[1]:
                names.append((int(index), suffix))

    names.sort(key=lambda item: item[0])
    if step>0:
        names = names[::-1]

    for item in names:
        old_name = "%s_%s%s" % (start[0], item[0], item[1])
        new_name = "%s_%s%s" % (start[0], item[0]+step, item[1])
        op = os.path.join(folder, old_name)
        np = os.path.join(folder, new_name)
        os.rename(op, np)

    print("Move OK!")

if __name__ == '__main__':
    folder = "imgs/0"
    start = (2, 11)
    step = 1
    move(folder, start, step)
