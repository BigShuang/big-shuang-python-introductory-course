def get_repeat_str(s1, s2):
    res = ""
    for c in s1:
        if c in s2:
            if c not in res:
                res += c

    return res


r = get_repeat_str("abcba", "adae")
print(r)
r = get_repeat_str("lihua", "zhangsan")
print(r)
