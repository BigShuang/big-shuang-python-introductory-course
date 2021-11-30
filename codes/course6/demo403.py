def check_row_complete(row):
    for cell in row:
        if cell=='':
            return False

    return True

def check_and_clear(board):
    has_complete_row = False
    r, c = len(board), len(board[0])
    for ri in range(r):
        if check_row_complete(board[ri]):
            # 当前行可消除
            if ri > 0:
                for cur_ri in range(ri, 0, -1):
                    board[cur_ri] = board[cur_ri-1][:]
                board[0] = ['' for j in range(c)]
            else:
                board[ri] = ['' for j in range(c)]

    # display
    for row in board:
        for cell in row:
            if cell:
                print(cell, end="")
            else:
                print("_", end="")

        print()

board = [
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
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
