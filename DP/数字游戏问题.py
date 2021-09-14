'''
问题分析：
给定两个正数 m，n （0<=m<=n），现在求，从 m 开始，只能 加1，或者乘以2最后得到n的最小操作次数。
if i%2==1 : dp[i]=min(dp[i-1]+1,dp[i])
if i%2==0: dp[i]=min(dp[i-1]+1,dp[i/2]+1)
'''


class Solution:
    def Solve(self, m, n):
        dp = [0 for _ in range(n+1)]
        dp[m] = 0
        for i in range(m + 1, 2 * m):
            dp[i] = dp[i - 1] + 1
        for i in range(2 * m, n + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2] + 1
        print(dp)


if __name__ == '__main__':
    solu = Solution()
    solu.Solve(3, 9)
