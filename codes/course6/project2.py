WELCOME = "Welcome to maze game!"
ENTER  = "Enter command: "
Invalid = "Invalid command"
WIN = "Win!Successfully walked out of the maze."
BYE = "Bye!"

DIRECTION = {
    # direction: (dr, dc)
    "w": (-1, 0),
    "a": (0, -1),
    "s": (1, 0),
    "d": (0, 1),
}


def read_maze_file(maze_file):
    """"""
    with open(maze_file, 'r') as f:
        fr = f.read()

    board = []
    lines = fr.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            row = [cell for cell in line]
            board.append(row)

    return board


def show_board(board):
    for row in board:
        for cell in row:
            print(cell, end="")

        print()


def get_rc(board, start_or_end):
    r, c = len(board), len(board[1])
    for ri in range(r):
        for ci in range(c):
            if board[ri][ci] == start_or_end:
                return [ri, ci]

    return None


def move(board, start, drc, step):
    r, c = len(board), len(board[1])
    sr, sc = start
    dr, dc = drc

    board[sr][sc] = "_"

    for i in range(step):
        new_r = sr + dr
        new_c = sc + dc
        if board[new_r][new_c] == "#":
            break

        if new_r < 0 or new_r >= r or new_c < 0 or new_c >= c:
            break

        sr = new_r
        sc = new_c

    start[0] = sr
    start[1] = sc
    board[sr][sc] = "S"


def main(maze_file):
    # 1. 获取迷宫对应的二维列表
    board = read_maze_file(maze_file)
    # 2. 获取起点和终点坐标
    start = get_rc(board, "S")  # r, c
    end = get_rc(board, "E")  # r, c

    # 3. 展示欢迎语
    print(WELCOME)

    # 4. 使用循环
    while True:
        # 4-a. 循环中展示面板
        show_board(board)

        if start == end:  # 4-b. 到达终点，胜利并结束游戏
            print(WIN)
            return

        # 4-c. 接受用户输入
        cmd = input(ENTER)
        cmd = cmd.lower()

        # 4-d. 处理用户输入
        if len(cmd) > 0:
            if cmd[0] == "e":  # 4-e. 直接退出游戏
                print(BYE)
                return

            # 4-f. 尝试解析移动命令
            direction = cmd[0]
            step = cmd[1:]
            if direction in DIRECTION:
                drc = DIRECTION[direction]
                if step.isdigit():  #
                    # 4-g. 解析成功，移动并直接进入下一轮循环
                    step = int(step)
                    move(board, start, drc, step)
                    continue

        # 4-h. 处理中失败了，提醒输入不符合规范。
        print(Invalid)


maze_file = "maze01.txt"
main(maze_file)