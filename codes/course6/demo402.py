def check_bunch_match(bunch, symbol):
    res = True
    for one in bunch:
        if one != symbol:
            res = False
            break

    return res


def get_ttt_winner(board):
    r, c = len(board), len(board[0])
    for symbol in "XO":
        for ri in range(r):
            row = board[ri]
            if check_bunch_match(row, symbol):
                return symbol

        for ci in range(c):
            column = [board[ri][ci] for ri in range(r)]
            if check_bunch_match(column, symbol):
                return symbol

        diagonal_1 = [board[ri][ri] for ri in range(r)]
        diagonal_2 = [board[ri][c-ri-1] for ri in range(r)]
        if check_bunch_match(diagonal_1, symbol):
            return symbol
        if check_bunch_match(diagonal_2, symbol):
            return symbol

    return "N"


# board1 = [
#     ["X", "X", "X"],
#     ["O", "X", " "],
#     ["O", " ", "O"],
# ]

# r = get_ttt_winner(board1)
# print(r)

# r1 = check_bunch_match(["X", "X", "X"], "X")
# r2 = check_bunch_match(["O", " ", "O"], "O")
# r3 = check_bunch_match(["X", "X", "X"], "O")
# r4 = check_bunch_match(["X", "X", "O"], "X")
# print(r1, r2, r3, r4)

board1 = [
    ["X", "X", "X"],
    ["O", "X", " "],
    ["O", " ", "O"],
]
print(get_ttt_winner(board1))

board2 = [
    ["X", "O", "X"],
    ["O", "X", " "],
    ["O", "X", "O"],
]
print(get_ttt_winner(board2))

board3 = [
    ["X", " ", "X"],
    ["O", "X", "X"],
    ["O", "O", "O"],
]
print(get_ttt_winner(board3))