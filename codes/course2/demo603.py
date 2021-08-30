courses = ["language", "math", "english"]

scores = [
    ["A", 90, 80, 85],
    ["B", 80, 87, 86],
    ["C", 85, 90, 90]
]


# 5
courses.append("sports")
sports_scores = (85, 90, 85)
for i in range(len(scores)):
    item = scores[i]
    item.append(sports_scores[i])


# 6
courses.append("music")
courses.append("art")
courses.append("science")

music_scores = (-1, 90, -1)
art_scores = (-1, -1, 95)
science_scores = (90, -1, -1)

for i in range(len(scores)):
    item = scores[i]
    item.append(music_scores[i])
    item.append(art_scores[i])
    item.append(science_scores[i])


# 2
name = "A"
for item in scores:
    item_name = item[0]
    if item_name == name:
        # 用output变量来计算最后的输出
        output = "name: %s" % item_name
        for i in range(len(courses)):
            # 遍历所有课程的索引
            si = i + 1  # 成绩的索引为课程索引+1
            if item[si] >= 0:
                # 如果成绩值不小于0，就代表选择了这门课程
                course = courses[i]
                output += ", %s: %s" % (course, item[si])
        output += "."
        print(output)


# 3
d_item = ("D", 80, 85, 85, 85, -1, -1, 85)
scores.append(d_item)


# 4
for item in scores:
    item_name = item[0]
    # 用s来计算总分
    s = 0
    # 用output变量来计算对应的输出
    output = "%s: " % item_name
    for i in range(len(courses)):
        # 遍历所有课程的索引
        si = i + 1  # 成绩的索引为课程索引+1
        if item[si] >= 0:
            # 如果成绩值不小于0，就代表选择了这门课程
            course = courses[i]
            output += "%s=%s, " % (course, item[si])
            s += item[si]
    output += "sum=%s." % s
    print(output)
