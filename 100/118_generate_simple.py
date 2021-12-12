'''
118. 杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。





示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]


提示:

1 <= numRows <= 30
'''


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        ret = []
        for i in range(0, numRows):
            ret.append([])
            for j in range(0, i + 1):
                if j == 0:
                    ret[i].append(1)
                    continue
                if j == i:
                    ret[i].append(1)
                    continue
                ret[i].append(ret[i - 1][j - 1] + ret[i - 1][j])
        return ret


solve = Solution()
numRows = 0
numRows = 1
numRows = 2
result = solve.generate(numRows)
print(result)
