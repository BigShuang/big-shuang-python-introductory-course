WELCOME = "Welcome to maze game!"
ENTER  = "Enter command: "
Invalid = "Invalid command"
WIN = "Win!Successfully walked out of the maze."
BYE = "Bye!"


DIRECTION = {
    "w": [-1, 0], # r, c
    "a": [0, -1],  # r, c
    "s": [1, 0],  # r, c
    "d": [0, 1],  # r, c
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
            if cell == "X":
                cell = "#"
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
    board = read_maze_file(maze_file)
    start = get_rc(board, "S")  # r, c
    end = get_rc(board, "E")  # r, c


    print(WELCOME)
    while True:
        show_board(board)

        if start == end:
            print(WIN)
            return

        cmd = input(ENTER)
        cmd = cmd.lower()

        if len(cmd) > 0:
            if cmd[0] == "e":
                print(BYE)
                return

            direction = cmd[0]
            step = cmd[1:]
            if direction in DIRECTION:
                drc = DIRECTION[direction]
                if step.isdigit():
                    step = int(step)
                    move(board, start, drc, step)
                    continue

        print(Invalid)


maze_file = "maze01.txt"
main(maze_file)