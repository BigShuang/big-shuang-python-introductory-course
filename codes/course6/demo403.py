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
    for cell in row:
        if cell == "":
            return False

    return True


def check_and_clear(board):
    r, c = len(board), len(board[0])
    to_del_row = []
    for ri in range(r):
        if check_row_complete(board[ri]):
            to_del_row.append(ri)

    for ri in to_del_row[::-1]: # reverse
        board.pop(ri)

    for _ in to_del_row:
        # 每次生成新的row，不会相互干扰
        row = ['' for ci in range(c)]
        board.insert(0, row)

    # display
    show_board(board)

board1 = [
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

check_and_clear(board1)


# show_board(board)