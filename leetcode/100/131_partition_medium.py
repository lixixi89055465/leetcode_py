'''
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。



示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]


提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

'''


class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(0, n - i):
                dp[j][j + i] = s[j] == s[j + i] and dp[j + 1][j + i - 1]
        ans = []
        ret = []

        def dfs(i):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret


solve = Solution()
s = "aabb"
# s = "efe"
result = solve.partition(s)
print(result)
