def check_all_even(nums):
    # 检查是否全都是偶数
    for num in nums:
        if num % 2 == 1:
            return False

    return True
