def show_board(board):
    for row in board:
        for cell in row:
            if cell == "":
                print("_", end="")
            else:
                print(cell, end="")
        print()


def check_row_complete(row):
    # 检查一行是否已经填满俄罗斯方格，已填满则返回True，否则返回False
    # TODO
    pass


def check_and_clear(board):
    r, c = len(board), len(board[0])
    for ri in range(r):
        if check_row_complete(board[ri]):
            # TODO
            pass

    # display
    show_board(board)

board = [
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', 'L', '', '', '', ''],
    ['', '', '', '', '', 'L', 'L', 'L', '', '', '', ''],
    ['', '', 'I', '', 'Z', 'Z', 'Z', 'Z', '', '', '', 'Z'],
    ['', 'T', 'I', 'I', 'S', 'Z', 'Z', 'Z', 'Z', '', 'Z', 'Z'],
    ['T', 'T', 'I', 'I', 'S', 'S', 'S', 'T', 'T', 'T', 'Z', 'L'],
    ['J', 'T', 'I', 'I', 'J', 'S', 'S', 'S', 'T', 'L', 'L', 'L'],
    ['J', 'J', 'J', 'I', 'J', 'J', 'J', 'S', 'I', 'I', 'I', 'I']
]

check_and_clear(board)
# show_board(board)