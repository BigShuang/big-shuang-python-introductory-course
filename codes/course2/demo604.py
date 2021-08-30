scores = {
    "A": {
        "language":90,
        "math":80,
        "english":85
    },
    "B": {
        "language":80,
        "math":87,
        "english":86
    },
    "C": {
        "language":85,
        "math":90,
        "english":90
    }
}


# 5
sports_scores = {
    "A": 85,
    "B": 90,
    "C": 85
}
for name in scores:
    info = scores[name]
    info["sports"] = sports_scores[name]


# 6

add_scores = {
    "A": {
        "science": 90
    },
    "B": {
        "music": 90
    },
    "C": {
        "art": 95
    }
}

for name in scores:
    info = scores[name]
    new_info = add_scores[name]
    info.update(new_info)


# 2
name = "A"
score_a = scores[name]
output = "name: %s" % name
for key in score_a:  # key即是该同学选择的课程的名称
    output += ", %s: %s" % (key, score_a[key])
output += "."

print(output)


# 3
score_d = {
    "language": 80,
    "math": 85,
    "english": 85,
    "sports": 85,
    "science": 85
}

scores["D"] = score_d

# 4
for name in scores:
    info = scores[name]
    output = "%s: " % name
    s = 0
    for key in info:  # key即是该同学选择的课程的名称
        output += "%s=%s, " % (key, info[key])
        s += info[key]

    output += "sum=%s." % s
    print(output)

