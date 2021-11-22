SCORE_FILE = "scores.txt"

MAIN_MENU = """Welcome!
You can enter `f`, `c`, `u`, `l` or `e`.
The meaning is as follows
- f: filter student by a score
- c: create score
- u: update score
- l: show all student with scores
- e: exit
Enter your command: """
INVALID = "Invalid Input."

def read_scores(score_file):
    return {}


SCORES = read_scores(SCORE_FILE)


def filter_score():
    pass


def create_score():
    pass


def update_score():
    pass


def show_all():
    pass


def save():
    pass


def main():
    while True:
        print(MAIN_MENU)
        cmd = input()
        if cmd == "f":
            filter_score()
        elif cmd == "c":
            create_score()
        elif cmd == "u":
            update_score()
        elif cmd == "l":
            show_all()
        elif cmd == "e":
            save()
            break
        else:
            print(INVALID)


main()