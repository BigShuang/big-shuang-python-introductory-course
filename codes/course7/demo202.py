WELCOME = "Welcome to Tic-Tac-Toe!"
ENTER  = "%s's turn. Enter row index and column index to place (ri, ci):\n"
Invalid = "Invalid command."
Used = "The place is already occupied."


class Game:
    def __init__(self):
        self.current = "X"

        self.board = [
            [" " for ci in range(3)] for ri in range(3)
        ]

    def show_board(self):
        for ri, row in enumerate(self.board):

            row_str = ""
            for ci, cell in enumerate(row):
                row_str += " %s " % cell
                if ci != 2:
                    row_str += "|"
            print(row_str)

            if ri != 2:
                print("---+---+---")

    def check_bunch_match(self, bunch):
        res = True
        for one in bunch:
            if one != self.current:
                res = False
                break

        return res

    def check_win(self):
        r, c = len(self.board), len(self.board[0])
        for ri in range(r):
            row = self.board[ri]
            if self.check_bunch_match(row):
                return True

        for ci in range(c):
            column = [self.board[ri][ci] for ri in range(r)]
            if self.check_bunch_match(column):
                return True

        diagonal_1 = [self.board[ri][ri] for ri in range(r)]
        diagonal_2 = [self.board[ri][c - ri - 1] for ri in range(r)]
        if self.check_bunch_match(diagonal_1):
            return True
        if self.check_bunch_match(diagonal_2):
            return True

        return False

    def turn_player(self):
        if self.current == "X":
            self.current = "O"
        else:
            self.current = "X"

    def parse_rc(self, cmd):
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

    def run(self):
        print(WELCOME)
        while True:
            self.show_board()
            cmd = input(ENTER % self.current)
            ri, ci = self.parse_rc(cmd)
            if ri >= 0:
                if self.board[ri][ci] == " ":
                    self.board[ri][ci] = self.current
                    if self.check_win():
                        self.show_board()
                        print("%s win!" % self.current)
                        return

                    self.turn_player()
                else:
                    print(Used)
            else:
                print(Invalid)


game = Game()
game.run()