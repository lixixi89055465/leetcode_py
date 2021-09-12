'''
triangle

'''


class Solution:
    def minimumTotal1(self, triangle):
        m = len(triangle)
        n = len(triangle[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n - 1, 0, -1):
            for j in range(0, i):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0]

    def minimumTotal2(self, triangle):
        N = triangle.size()
        dp = [0 for _ in range(N)]
        for i in range(N - 1, 0, -1):
            for j in range(0, i):
                dp[j] = min(dp[j], dp[j + 1] + triangle[i][j])

        return dp[0]

    def minimumTotal3(self, triangle):
        N = triangle.size()
        return self.helper(0, 0, triangle, [[0 for _ in range(N)] for _ in range(N)])

    def helper(self, row, col, triange, memo):
        if row >= triange.size:
            return 0
        if memo[row][col] != 0:
            return memo[row][col]
        return memo[row][col] - min(self.helper(row + 1, col, triange, memo),
                                    self.helper(row + 1, col + 1, triange, memo)) + triange[row][col]


solve = Solution()
solve.minimumTotal2()
