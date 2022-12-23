def check_row_complete(row):
    # 检查一行是否已经填满俄罗斯方格，已填满则返回True，否则返回False
    for cell in row:
        if cell == "":
            return False

    return True


def show_board(board):
    for row in board:
        for cell in row:
            if cell == "":
                print("_", end="")
            else:
                print(cell, end="")
        print()


def check_and_clear(board):
    r, c = len(board), len(board[0])
    for ri in range(r):
        if check_row_complete(board[ri]):
            if ri > 0:
                for cur_ri in range(ri, 0, -1):
                    board[cur_ri] = board[cur_ri - 1][:]
                board[0] = ['' for j in range(c)]
            else:
                board[ri] = ['' for j in range(c)]

    # display
    show_board(board)

board2 = [
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', 'L', '', '', '', ''],
    ['', '', '', '', '', 'L', 'L', 'L', '', '', '', ''],
    ['T', 'T', 'I', 'I', 'S', 'S', 'S', 'T', 'T', 'T', 'Z', 'L'],
    ['', '', 'I', '', 'Z', 'Z', 'Z', 'Z', '', '', '', 'Z'],
    ['J', 'T', 'I', 'I', 'J', 'S', 'S', 'S', 'T', 'L', 'L', 'L'],
    ['', 'T', 'I', 'I', 'S', 'Z', 'Z', 'Z', 'Z', '', 'Z', 'Z'],
    ['J', 'J', 'J', 'I', 'J', 'J', 'J', 'S', 'I', 'I', 'I', 'I']
]

check_and_clear(board2)
# show_board(board)