'''
minimum path sum
'''


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for 0 in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m][n]

    def minPathSum1(self, grid):
        M = grid.length
        N = grid[0].length
        memo = [[0 for _ in range(N)] for _ in range(M)]
        return self.helper(grid, M - 1, N - 1, memo)

    def helper(self, grid, i, j, memo):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return 100000
        if memo[i][j] > 0:
            return memo[i][j]
        return grid[i][j] + min(
            self.helper(grid, i - 1, j, memo),
            self.helper(grid, i, j - 1, memo)
        )

