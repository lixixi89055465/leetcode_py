'''
931. 下降路径最小和
给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。



示例 1：

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：下面是两条和最小的下降路径，用加粗+斜体标注：
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
示例 2：

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：下面是一条和最小的下降路径，用加粗+斜体标注：
[[-19,57],
 [-40,-5]]
示例 3：

输入：matrix = [[-48]]
输出：-48


提示：

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

'''


class Solution:
    def minFallingPathSum2(self, A: list) -> int:
        N = len(A)
        for r in range(N - 2, 0, -1):
            for c in range(N):
                minValue = A[r + 1][c]
                if c > 0:
                    minValue = min(minValue, A[r + 1][c - 1])
                if c + 1 < N:
                    minValue = min(minValue, A[r + 1])
                A[r][c] += minValue
        res = 100000000
        return min(A[0])

    def minFallingPathSum1(self, matrix: list) -> int:
        n = len(matrix)
        dp1 = matrix[0][:]
        dp2 = matrix[0][:]
        for i in range(1, n):
            dp2 = matrix[i][:]
            for j in range(n):
                if j == 0:
                    dp2[j] = min(dp1[j], dp1[j + 1]) + dp2[j]
                elif j == n - 1:
                    dp2[j] = min(dp1[j], dp1[j - 1]) + dp2[j]
                else:
                    dp2[j] = min(dp1[j - 1], dp1[j], dp1[j + 1]) + dp2[j]
            dp1 = dp2[:]
        return min(dp1)


solve = Solution()
# matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
matrix = [[-19, 57], [-40, -5]]
result = solve.minFallingPathSum(matrix)
print(result)
