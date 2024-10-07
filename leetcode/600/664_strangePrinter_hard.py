'''
664. 奇怪的打印机
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。


示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。


提示：

1 <= s.length <= 100
s 由小写英文字母组成
'''

from functools import reduce


class Solution:
    def strangePrinter(self, s):
        len1 = len(s)
        dp = [[1 for _ in range(len1)] for _ in range(len1)]
        for i in range(1, len1):
            for j in range(0, len1 - i):
                if s[j] == s[i + j]:
                    dp[j][j + i] = dp[j][j + i - 1]
                else:
                    dp[j][j + i] = reduce(lambda x, y: min(x, y),
                                          [dp[j][j + x] + dp[j + x + 1][j + i] for x in range(0, i)])
        return dp[0][len1 - 1]


# s = "aba"
s = "aaabbb"
solve = Solution()
result = solve.strangePrinter(s)
print(result)