import os

hanzi = "一二三四五六七八九"

yaml = """---
title: big shuang python introductory course
author: Big Shuang
header: course blog - https://www.cnblogs.com/BigShuang/p/14887595.html
footer: No. ${pageNo} / ${pageCount}
---

"""


paging = '<div style="page-break-after:always"></div>'

def merge_md(folder, title):
    files = os.listdir(folder)

    text = yaml
    text += "# %s\n " % title
    text += paging+ "\n"
    for file in files:
        name, suffix = os.path.splitext(file)
        if name.isdigit():
            index = int(name) - 1
            file_title = "## 第%s节" % hanzi[index]
            fp = os.path.join(folder, file)
            with open(fp, "r", encoding="utf-8") as f:
                ft = f.read()

            text += file_title + ft[2:] + "\n"
            text += paging+ "\n"

    out = os.path.join(folder, "merge_all.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)

    print("Merge Done")


if __name__ == '__main__':
    folder = "contents/2"
    title = "第二章 容器"
    merge_md(folder, title)
