"""
将img文件夹的图片名称序号，
批量往前或往后移动指定数值
"""

import os
import time


TIME_SPACE = 0.6


def get_valid_path(root, folder):
    if os.path.exists(folder):
        return folder

    if os.path.exists(root+folder):
        return root + folder

    raise Exception("Not Found Folder: %s, %s" % (root, folder))


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
        print("rename: %s->%s"%(op, np))
        time.sleep(TIME_SPACE)

    print("Move OK!")


if __name__ == '__main__':
    folder_path = get_valid_path("../", "imgs/0")
    start = (3, 11)
    step = -1
    move(folder_path, start, step)
