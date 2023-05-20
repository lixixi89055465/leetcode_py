'''
119. 杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。





示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:

输入: rowIndex = 0
输出: [1]
示例 3:

输入: rowIndex = 1
输出: [1,1]


提示:

0 <= rowIndex <= 33


进阶：

你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
'''


class Solution:
    def getRow(self, numRows: int):
        ret = [0] * (numRows + 1)
        ret[0]=1
        for i in range(1, numRows+1):
            ret[i]=ret[i-1]*(numRows-i+1)//i
        return ret


solve = Solution()
numRows = 3
result = solve.getRow(numRows)
print(result)
