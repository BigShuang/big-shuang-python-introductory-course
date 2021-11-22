def get_num():
    num = input("Please enter a num: ")
    while not num.isdigit():
        num = input("Please enter a num: ")

    return num


def select_course():
    courses = ["math", "music", "grammar", "history"]

    course = input("Please select a course: ")
    while course not in courses:
        print("Invalid selection: %s" % course)
        course = input("Please select a course: ")

    return course
