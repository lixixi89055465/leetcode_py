'''
132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。



示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1


提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成
'''


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(n - i):
                dp[i][i + j] = s[i] == s[i + j] and dp[j + 1][j + i - 1]
        ret = [0] * n
        for i in range(1, n):
            ret[i] = ret[i - 1] + 1
            for j in range(i):
                if dp[j][i]:
                    ret[i] = ret[j] + dp[j][i]
        print(ret)


solve = Solution()
s = "efe"
result = solve.minCut(s)
print(result)
