SCORE_FILE = "scores.txt"

MAIN_MENU = """---------------
欢迎！你可以输入`c`、`f`、`u`、`l`、`e`命令, 意义如下:
- c: 新建学生
- f: 查询大于等于某成绩的所有学生
- u: 修改学生分数
- l: 展示所有学生分数
- e: 退出
请输入命令: """
INVALID = "输入无效"

FILTER_MENU1 = "请输入查询分: "
UPDATE_MENU1 = "请输入学生名字: "
UPDATE_MENU2 = "请输入学生分数: "
UPDATE_MENU3 = "修改成功。"

CREATE_MENU1 = "请输入新增学生姓名: "
CREATE_MENU2 = "请输入新增学生分数: "
CREATE_MENU_R1 = "名字已存在，无法创建。"
CREATE_MENU_R2 = "成功新增学生分数。"


SHOW_MENU1 = "学生成绩: "
EXIT_MENU = "再见"


def read_scores(score_file):
    scores = {}

    with open(score_file, 'r') as f:
        fr = f.read()

    lines = fr.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            name, score = line.split(",")
            score = int(score)
            scores[name] = score

    return scores


def show_all(scores, filter_value=0):
    print(SHOW_MENU1)
    for name in scores:
        score = scores[name]
        if score >= filter_value:
            print("{:<15s}: {}".format(name, score))


def filter_score(scores):
    while True:
        score = input(FILTER_MENU1)
        if score.isdigit():
            score = int(score)
            show_all(scores, filter_value=score)
            return
        else:
            print(INVALID)


def update_score(scores):
    while True:
        name = input(UPDATE_MENU1)
        if name not in scores:
            print(INVALID)
        else:
            break

    while True:
        score = input(UPDATE_MENU2)
        if score.isdigit():
            score = int(score)
            scores[name] = score
            print(UPDATE_MENU3)
            return
        else:
            print(INVALID)


def save(score_file, scores):
    with open(score_file, 'w') as f:
        for name in scores:
            score = scores[name]
            f.write("{},{}\n".format(name, score))


def create_score(scores):
    while True:
        name = input(CREATE_MENU1)
        if name in scores:
            print(CREATE_MENU_R1)
        else:
            break

    while True:
        score = input(CREATE_MENU2)
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                scores[name] = score
                print(CREATE_MENU_R2)
                return

        print(INVALID)


def main(score_file):
    scores = read_scores(score_file)
    while True:
        cmd = input(MAIN_MENU)
        if cmd == "f":
            filter_score(scores)
        elif cmd == "c":
            create_score(scores)
        elif cmd == "u":
            update_score(scores)
        elif cmd == "l":
            show_all(scores)
        elif cmd == "e":
            save(score_file, scores)
            print(EXIT_MENU)
            break
        else:
            print(INVALID)



main(SCORE_FILE)