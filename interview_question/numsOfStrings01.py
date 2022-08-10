'''
numsOfStrings

3.小红的字符串计数-腾讯娱乐集团2022暑期实习生招聘技术类岗位
'''


class Solution:
    def numsOfStrings(self, n, k):
        if k*2>n:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 0
        dp[1][0] = 0
        dp[2][1] = 26
        cheng = 10 ** 6
        for i in range(3, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i - 1][j] + 25 * dp[i - 2][j - 1]) % cheng
        return dp[n][k]


solve = Solution()
n = 4
k = 2# 1300
n = 4
k = 1# 1300
n = 4
k = 2# 1300
result = solve.numsOfStrings(n=n, k=k)
print(result)
