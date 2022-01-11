def check_all_even(nums):
    # 检查是否全都是偶数
    for num in nums:
        if num % 2 == 1:
            return False

    return True

def check_all_odd(nums):
    # 检查是否全都是奇数
    for num in nums:
        if num % 2 == 0:
            return False

    return True

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None

class AdvancedNode(Node):
    def __init__(self, num):
        super().__init__(num)
        self.prev = None
