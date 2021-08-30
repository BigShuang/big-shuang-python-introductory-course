scores = {
    "A": (90, 80, 85),
    "B": (80, 87, 86),
    "C": (85, 90, 90)
}


name = "A"
score_a = scores[name]
print("name: %s, language: %s, math: %s, english: %s." %
      (name, score_a[0], score_a[1], score_a[2]))

scores["D"] = (80, 85, 85)

for name in scores:
    s1, s2, s3 = scores[name]
    s = s1 + s2 + s3
    print("%s: language=%s, math=%s, english=%s, sum=%s." %
          (name, s1, s2, s3, s))

