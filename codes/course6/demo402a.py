def check_bunch_match(bunch, symbol):
    """
    判断 bunch 这一串棋子，是否都由symbol对应的棋子组成
    :param bunch: 一串棋子，三个棋子字符组成的列表
    :param symbol: 玩家棋子符号, "X" 或 "O"
    :return: bunch中的棋子都为 symbol，则返回 True，否则返回 False
    """
    pass


def get_ttt_winner(board):
    """
    :param board: 棋盘， 3x3的二维列表
    :return: 胜利玩家对应的字母"X"或者"O"， 没有胜利者则返回 "N"
    """
    r, c = len(board), len(board[0])
    for symbol in "XO":
        # 判断所有行
        for ri in range(r):
            row = [] # TODO
            if check_bunch_match(row, symbol):
                return symbol

        # 判断所有列
        for ci in range(c):
            column = [] # TODO
            if check_bunch_match(column, symbol):
                return symbol

        # 判断两个对角线
        diagonal_1 = [] # TODO
        diagonal_2 = [] # TODO
        if check_bunch_match(diagonal_1, symbol):
            return symbol
        if check_bunch_match(diagonal_2, symbol):
            return symbol

    return "N"


board = [
    ["X", "X", "X"],
    ["O", "X", " "],
    ["O", " ", "O"],
]

r = get_ttt_winner(board)
print(r)
