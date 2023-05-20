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

    def getMax(self, heights):
        s = []
        i = 0
        n = len(heights)
        left, right = [0] * n, [n] * n
        while i < n:
            # while s and heights[i] < heights[s[-1]]:
            while s and heights[s[-1]] > heights[i]:
                right[s[-1]] = i
                s.pop()
            left[i] = s[-1] if s else -1
            s.append(i)
            i += 1
        ret = max([(right[i] - left[i] - 1) * heights[i] for i in range(n)]) if n > 0 else 0
        return ret

    def maximalRectangle(self, matrix: list) -> int:
        if len(matrix)==0:
            return 0
        heights = [0] * len(matrix[0])
        maxS = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            maxS = max(maxS, self.getMax(heights))
        return maxS


solve = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = []
# matrix = [["0"]]
# matrix = [["1"]]
matrix = [["0","0"]]
result = solve.maximalRectangle(matrix)
print(result)
