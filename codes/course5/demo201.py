scores = {
    "math": 80,
    "history": 70,
    "chemistry": 75
}


for course in scores:
    score = scores[course]
    print("%10s: %s" %(course, score))

# for course in scores:
#     score = scores[course]
#     print("{:10s}: {}".format(course, score))

# for course in scores:
#     score = scores[course]
#     print(f"{course:10s}: {score}")