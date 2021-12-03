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
    pass


def show_board(board):
    pass


def get_rc(board, start_or_end):
    pass


def move(board, start, drc, step):
    pass


def main(maze_file):
    pass


maze_file = "maze01.txt"
main(maze_file)