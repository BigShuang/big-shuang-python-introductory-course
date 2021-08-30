"""
"""

scores = [
    ("A", 90, 80, 85),
    ("B", 80, 87, 86),
    ("C", 85, 90, 90)
]


name = "A"
for item in scores:
    item_name = item[0]
    if item_name == name:
        print("name: %s, language: %s, math: %s, english: %s." % item)

d_item = ("D", 80, 85, 85)
scores.append(d_item)

for item in scores:
    name, s1, s2, s3 = item
    s = s1 + s2 + s3
    print("%s: language=%s, math=%s, english=%s, sum=%s." %
          (name, s1, s2, s3, s))
