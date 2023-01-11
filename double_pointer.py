# Form ChatGPT
def find_two_sum(numbers, target):
    # 初始化两个指针
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            # 找到了两个数字
            return (numbers[left], numbers[right])
        elif sum < target:
            # 和太小，需要增大
            left += 1
        else:
            # 和太大，需要减小
            right -= 1
    # 没有找到两个数字
    return None

# 调用函数
result = find_two_sum([1, 2, 3, 4, 5], 7)
print(result)  # 输出 (2, 5)
