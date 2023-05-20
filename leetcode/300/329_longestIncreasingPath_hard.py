'''
329. 矩阵中的最长递增路径
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。



示例 1：


输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

'''

from collections import *


class Solution:
    def longestIncreasingPath(self, matrix):
        edgesRu = defaultdict(list)
        edgesChu = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0 and matrix[i][j] < matrix[i - 1][j]:
                    edgesChu[(i, j)].append((i - 1, j))
                    edgesRu[(i - 1, j)].append((i, j))
                if i != len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
                    edgesChu[(i, j)].append((i + 1, j))
                    edgesRu[(i + 1, j)].append((i, j))
                if j != 0 and matrix[i][j] < matrix[i][j - 1]:
                    edgesChu[(i, j)].append((i, j - 1))
                    edgesRu[(i, j - 1)].append((i, j))
                if j != len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1]:
                    edgesChu[(i, j)].append((i, j + 1))
                    edgesRu[(i, j + 1)].append((i, j))
        flag = 1
        while len(edgesRu) > 0:
            flag += 1
            delK = []
            for i in edgesChu:
                if i not in edgesRu:
                    delK.append(i)
            for k in delK:
                for j in edgesChu[k]:
                    edgesRu[j].remove(k)
                    if len(edgesRu[j]) == 0:
                        edgesRu.pop(j)
                edgesChu.pop(k)
        return flag


solve = Solution()
# matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# matrix = [[1]]
result = solve.longestIncreasingPath(matrix)
print(result)
