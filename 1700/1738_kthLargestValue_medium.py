'''
1738. 找出第 K 大的异或坐标值
给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。

矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。

请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。



示例 1：

输入：matrix = [[5,2],[1,6]], k = 1
输出：7
解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
示例 2：

输入：matrix = [[5,2],[1,6]], k = 2
输出：5
解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
示例 3：

输入：matrix = [[5,2],[1,6]], k = 3
输出：4
解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
示例 4：

输入：matrix = [[5,2],[1,6]], k = 4
输出：0
解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
'''


class Solution:
    def insertAndSort(self, result, tMatrix, k):
        lenr = len(result)
        left = 0
        right = lenr
        while left < right:
            mid = (left + right) // 2
            if result[mid] < tMatrix:
                left = mid + 1
            elif result[mid] > tMatrix:
                right = mid - 1

    def kthLargestValue(self, matrix, k):
        tMatrix = [0] * len(matrix) * len(matrix[0])
        print(tMatrix)
        width = len(matrix[0])
        height = len(matrix)
        result = []
        minloc = 0
        tMatrix[0] = (matrix[0][0], (0, 0))
        for i in range(1, len(matrix[0])):
            tMatrix[i] = (matrix[0][i] ^ tMatrix[i - 1][0], (0, i))
        for i in range(1, len(matrix)):
            tMatrix[i * width] = (matrix[i][0] ^ tMatrix[(i - 1) * width][0], (i, 0))

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                tMatrix[i * width + j] = (tMatrix[(i - 1) * width + j][0] ^ tMatrix[i * width + j - 1][0] ^ tMatrix[
                    (i - 1) * width + j - 1][0] ^ matrix[i][j], (i, j))
        print(tMatrix)
        tMatrix = sorted(tMatrix, key=lambda x: x[0], reverse=True)
        return tMatrix[k][0]


def cri(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    return 0


matrix = [[5, 2], [1, 6]]
k = 2
solve = Solution()
result = solve.kthLargestValue(matrix, k)
print(result)
