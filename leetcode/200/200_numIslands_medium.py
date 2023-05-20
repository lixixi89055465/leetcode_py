'''
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class UnionSet:
    def __init__(self, n):
        self.parents = [-1 for i in range(n + 1)]

    def find(self, index):
        while self.parents[index] != -1 and self.parents[index] != index:
            index = self.parents[index]
        return index

    def union(self, index1, index2):
        parent1 = self.find(index1)
        parent2 = self.find(index2)
        if parent2 == parent1:
            return
        self.parents[parent2] = parent1


class Solution:
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        us = UnionSet(row * col)

        def node(i, j):
            return i * col + j

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                us.parents[node(i, j)] = node(i, j)
                if i != 0 and grid[i - 1][j] == '1':
                    us.union(node(i, j), node(i - 1, j))
                if j != 0 and grid[i][j - 1] == '1':
                    us.union(node(i, j), node(i, j - 1))
                if i != row - 1 and grid[i + 1][j] == '1':
                    us.union(node(i, j), node(i + 1, j))
                if j != col - 1 and grid[i][j + 1] == '1':
                    us.union(node(i, j), node(i, j + 1))
        ans = []
        for i in range(len(us.parents)):
            if us.parents[i] >= 0 and us.find(i) not in ans:
                ans.append(us.find(i))
        return len(ans)


solve = Solution()
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]]
# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
result = solve.numIslands(grid)
print(result)
