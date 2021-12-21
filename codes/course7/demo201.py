WELCOME = "Welcome to Tic-Tac-Toe!"
ENTER  = "%s's turn. Enter row index and column index to place (ri, ci):\n"
Invalid = "Invalid command."
Used = "The place is already occupied."


class Game:
    def __init__(self):
        self.board = []
        self.current = "X"

    def generate_board(self):
        pass

    def show_board(self):
        pass

    def check_bunch_match(self, bunch):
        return False

    def check_win(self):
        return False

    def place(self, ri, ci):
        return True

    def turn(self):
        pass

    def parse_rc(self, cmd):
        return -1, -1

    def run(self):
        while True:
            pass


game = Game()
game.run()