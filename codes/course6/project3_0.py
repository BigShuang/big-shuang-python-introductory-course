WELCOME = "Welcome to Tic-Tac-Toe!"
ENTER  = "%s's turn. Enter row index and column index to place (ri, ci):\n"
Invalid = "Invalid command."
Used = "The place is already occupied."


def generate_board():
    return


def show_board(board):
    pass


def parse_rc(cmd):
    return -1, -1


def check_bunch_match(bunch, symbol):
    return False


def check_win(board, symbol):
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
