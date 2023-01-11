"""
From ChatGPT
动态规划是一种常用的算法，用于解决最优化问题。

动态规划算法的基本思路是，将原问题分解成若干个子问题，并从这些子问题的解得到原问题的解。

举个例子，如果要求解最长公共子序列的问题，就可以使用动态规划的方法。

下面是 Python 代码的例子：
"""

def longest_common_subsequence(s1, s2):
    # 初始化动态规划数组
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 进行动态规划
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # 如果当前字符相同，则状态转移方程为 dp[i][j] = dp[i - 1][j - 1] + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 如果当前字符不同，则状态转移方程为 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 返回最长公共子序列的长度
    return dp[m][n]

# 调用函数
print(longest_common_subsequence('abcdef', 'acf'))  # 输出 3
print(longest_common_subsequence('abcdef', 'ghijk'))  # 输出 0
print(longest_common_subsequence('abcdef', 'bcd'))  # 输出 3

"""
在这个例子中，我们使用了一个二维数组 dp 来存储动态规划的状态，并通过循环来枚举每一个字符，并根据状态转移方程来更新数组的值。

状态转移方程是动态规划算法的核心，它决定了如何从子问题的解得到原问题的解。

在这个例子中，我们使用了两个字符串 s1 和 s2，并计算它们的最长公共子序列。我们的状态转移方程有两种情况：

如果当前字符 s1[i] 和 s2[j] 相同，则状态转移方程为 dp[i][j] = dp[i - 1][j - 1] + 1。这意味着如果当前字符相同，则最长公共子序列的长度加 1。

如果当前字符 s1[i] 和 s2[j] 不同，则状态转移方程为 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])。这意味着如果当前字符不同，则最长公共子序列的长度不变。

最后，我们通过返回 dp[m][n] 的值来得到最长公共子序列的长度。
"""