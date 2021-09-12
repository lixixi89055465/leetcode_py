'''
添加障碍
'''


class Solution:
    def uniquePathsWithObstackes(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for 0 in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i]:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


