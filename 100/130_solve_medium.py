'''
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。


示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]


提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'
'''


class UnionFind:
    def __init__(self, totalNodes):
        self.parents = [0 for i in range(totalNodes)]

    def find(self, index):
        while self.parents[index]:
            index = self.parents[index]
        return index

    def union(self, index1, index2):
        if self.find(index1) != self.find(index2):
            self.parents[self.find(index1)] = self.find(index2)

    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:

    def solve(self, board):
        def node(r, c):
            return r * cols + c

        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        uf = UnionFind(rows * cols + 1)
        dummyNode = rows * cols
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        uf.union(node(i, j), dummyNode)
                    else:
                        if i > 0 and board[i - 1][j] == 'O':
                            uf.union(node(i, j), node(i - 1, j))
                        if i < rows - 1 and board[i + 1][j] == 'O':
                            uf.union(node(i, j), node(i + 1, j))
                        if j > 0 and board[i][j - 1] == 'O':
                            uf.union(node(i, j), node(i, j - 1))
                        if j < cols - 1 and board[i][j + 1] == 'O':
                            uf.union(node(i, j), node(i, j + 1))
        for i in range(rows):
            for j in range(cols):
                if uf.isConnected(node(i, j), dummyNode):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board


solve = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
result = solve.solve(board)
print(result)
