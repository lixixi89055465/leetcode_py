'''
1240. 铺瓷砖
你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。

房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。

假设正方形瓷砖的规格不限，边长都是整数。

请你帮设计师计算一下，最少需要用到多少块方形瓷砖？



示例 1：



输入：n = 2, m = 3
输出：3
解释：3 块地砖就可以铺满卧室。
     2 块 1x1 地砖
     1 块 2x2 地砖
示例 2：



输入：n = 5, m = 8
输出：5
示例 3：



输入：n = 11, m = 13
输出：6


提示：

1 <= n <= 13
1 <= m <= 13
'''


class Solution:
    def __init__(self):
        self.ans = 0

    def tilingRectangle(self, n: int, m: int) -> int:
        matrix = [[False for _ in range(m)] for i in range(n)]
        self.dfs(matrix, 0, 0)

    def isValid(self, matrix, x, y, k):
        n = len(matrix)
        m = len(matrix[0])

        pass

    def dfs(self, matrix, x, y):
        if not matrix[x][y]:
            return
        n = len(matrix)
        m = len(matrix[0])
        for k in range(min(n - x, m - y)):
            if self.isValid(matrix, x, y, k):
                self.fill(matrix, x, y, k)
                if k == m - y:
                    self.dfs(matrix, x + 1, 0)
                else:
                    self.dfs(matrix, x, y + 1)
                self.reverseFill(matrix, x, y, k)


solution = Solution()
n = 11
m = 13
solution.tilingRectangle(n, m)
print(solution.ans)
