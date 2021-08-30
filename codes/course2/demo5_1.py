import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

a, b = 51 % 4, 51 // 4

c=[(3,'东'),(2,'南'),(1,'西'),(0,'北')]

# directions = {
#     0: "北",
#     1: "西",
#     2: "南",
#     3: "东",
# }

# dlist = ["北", "西", "南", "东"]

dlist = "北西南东"
direction = dlist[a]

print('小明面朝%s，转过了%s圈'%(direction, b))
