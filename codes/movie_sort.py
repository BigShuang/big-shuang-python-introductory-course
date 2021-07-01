"""
将img文件夹的图片名称序号，
批量往前或往后移动指定数值
"""

import os
import time


TIME_SPACE = 0.6



def rename_all(folder):
    movies = os.listdir(folder)
    names = []
    for m in movies:
        ms = m.split(".")
        print(ms)
        if len(ms) >= 3:
            new_name = "%s %s.%s" % (ms[0], ms[1], ms[-1])
            op = os.path.join(folder, m)
            np = os.path.join(folder, new_name)
            os.rename(op, np)
            print("rename: %s->%s"%(op, np))
            # break

    print("Move OK!")


if __name__ == '__main__':
    # folder = "F:\movie\****"
    # rename_all(folder)
    pass
