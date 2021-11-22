courses = ["math", "music", "grammar", "history"]

course = input("Please select a course: ")
while course not in courses:
    print("Invalid selection: %s" % course)
    course = input("Please select a course: ")


print("You select course: %s" % course)

