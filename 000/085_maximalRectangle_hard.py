'''
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。



示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0


提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
'''


class Solution:
    def maximalRectangle(self, matrix: list) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == 1:
                        dp[i][j] = (1, 1)
                    else:
                        dp[i][j] = (0, 0)
                    continue
                if matrix[i][j]==1:
                    h=min(dp[i-1][j][0]+1,1)
                    w=dp[i][j-1][1]+1
                    dp[i][j]=(h,w)
        for i in range(m):
            print(dp[i])
        return dp



solve = Solution()
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
result = solve.maximalRectangle(matrix)
print(result)
