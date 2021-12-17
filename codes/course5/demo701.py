SCORE_FILE = "scores.txt"

MAIN_MENU = """---------------
Welcome!
You can enter `c`, `f`, `u`, `l` or `e`.
The meaning is as follows
- c: create student score
- f: filter student by a score
- u: update score
- l: show all student with scores
- e: exit
Enter your command: """
INVALID = "Invalid Input."

FILTER_MENU1 = "Enter filter score: "
UPDATE_MENU1 = "Enter student name: "
UPDATE_MENU2 = "Enter student score: "
UPDATE_MENU3 = "Updated successfully."

CREATE_MENU1 = "Enter new student's name: "
CREATE_MENU2 = "Enter new student's score: "
CREATE_MENU_R1 = "The name already exists and cannot be created."
CREATE_MENU_R2 = "Successfully added student scores."

SHOW_MENU1 = "Students Scores: "
EXIT_MENU = "Bye"


def read_scores(score_file):
    scores = {}

    with open(score_file, 'r') as f:
        fr = f.read()

    lines = fr.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            name, score = line.split(",")
            score = int(score)
            scores[name] = score

    return scores


def show_all(scores, filter_value=0):
    print(SHOW_MENU1)
    for name in scores:
        score = scores[name]
        if score >= filter_value:
            print("{:<15s}: {}".format(name, score))


def filter_score(scores):
    while True:
        score = input(FILTER_MENU1)
        if score.isdigit():
            score = int(score)
            show_all(scores, filter_value=score)
            return
        else:
            print(INVALID)


def update_score(scores):
    while True:
        name = input(UPDATE_MENU1)
        if name not in scores:
            print(INVALID)
        else:
            break

    while True:
        score = input(UPDATE_MENU2)
        if score.isdigit():
            score = int(score)
            scores[name] = score
            print(UPDATE_MENU3)
            return
        else:
            print(INVALID)


def save(score_file, scores):
    with open(score_file, 'w') as f:
        for name in scores:
            score = scores[name]
            f.write("{},{}\n".format(name, score))


def create_score(scores):
    while True:
        name = input(CREATE_MENU1)
        if name in scores:
            print(CREATE_MENU_R1)
        else:
            break

    while True:
        score = input(CREATE_MENU2)
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                scores[name] = score
                print(CREATE_MENU_R2)
                return

        print(INVALID)


def main(score_file):
    scores = read_scores(score_file)
    while True:
        cmd = input(MAIN_MENU)
        if cmd == "f":
            filter_score(scores)
        elif cmd == "c":
            create_score(scores)
        elif cmd == "u":
            update_score(scores)
        elif cmd == "l":
            show_all(scores)
        elif cmd == "e":
            save(score_file, scores)
            print(EXIT_MENU)
            break
        else:
            print(INVALID)



main(SCORE_FILE)