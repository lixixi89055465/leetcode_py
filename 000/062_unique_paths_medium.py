'''

'''


class Solution:
    def uniquePaths0(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            dp[j][0] = 1;
        for j in range(n):
            dp[0][j] = 1;
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths1(self, m, n):
        dp = [0 for _ in range(n)]
        for j in range(m):
            dp[j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]

    def uniquePaths2(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        return self.helper(m - 1, n - 1, dp)

    def helper(self, m, n, dp):
        if n < 0 or m < 0:
            return 0
        if m == 0 and n == 0:
            return 1
        if dp[m][n] > 0:
            return dp[m][n]
        return self.helper(m - 1, n - 1, dp)
