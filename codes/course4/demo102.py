scores = {
    "A": {"music": 80, "history": 70, "grammer": 75},
    "B": {"music": 81, "history": 78, "grammer": 83},
    "C": {"music": 85, "history": 81, "grammer": 81},
    "D": {"music": 83, "history": 90, "grammer": 82},
}

def show_course_average(course_name):
    sum_score = 0
    for student in scores:
        student_scores = scores[student]
        course_score = student_scores[course_name]

        sum_score += course_score

    aver_score = sum_score / len(scores)

    print("Average score for %s course: %s" % (course_name, aver_score))

# show_course_average("music")
show_course_average("history")
show_course_average("grammer")
