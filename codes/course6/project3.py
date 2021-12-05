WELCOME = "Welcome to Tic-Tac-Toe!"
ENTER  = "%s's turn. Enter row index and column index to place (ri, ci):\n"
Invalid = "Invalid command."
Used = "The place is already occupied."


def generate_board():
    board = [
        [" " for ci in range(3)] for ri in range(3)
    ]

    return board


def show_board(board):
    for ri, row in enumerate(board):

        row_str = ""
        for ci, cell in enumerate(row):
            row_str += " %s " % cell
            if ci != 2:
                row_str += "|"
        print(row_str)

        if ri != 2:
            print("---+---+---")


def parse_rc(cmd):
    rc = cmd.split(",")
    if len(rc) == 2:
        ri, ci = rc
        ri = ri.strip()
        ci = ci.strip()
        if ci.isdigit() and ri.isdigit():
            ci = int(ci)
            ri = int(ri)
            if 0 <= ci < 3 and 0 <= ri < 3:
                return ri, ci

    return -1, -1


def check_bunch_match(bunch, symbol):
    res = True
    for one in bunch:
        if one != symbol:
            res = False
            break

    return res


def check_win(board, symbol):
    r, c = len(board), len(board[0])
    for ri in range(r):
        row = board[ri]
        if check_bunch_match(row, symbol):
            return True

    for ci in range(c):
        column = [board[ri][ci] for ri in range(r)]
        if check_bunch_match(column, symbol):
            return True

    diagonal_1 = [board[ri][ri] for ri in range(r)]
    diagonal_2 = [board[ri][c-ri-1] for ri in range(r)]
    if check_bunch_match(diagonal_1, symbol):
        return True
    if check_bunch_match(diagonal_2, symbol):
        return True

    return False


def main():
    board = generate_board()
    print(WELCOME)

    turn = "X"
    while True:
        show_board(board)
        cmd = input(ENTER % turn)
        ri, ci = parse_rc(cmd)
        if ri >= 0:
            if board[ri][ci] == " ":
                board[ri][ci] = turn

                if check_win(board, turn):
                    show_board(board)
                    print("%s win!" % turn)
                    return

                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
            else:
                print(Used)
        else:
            print(Invalid)


main()
