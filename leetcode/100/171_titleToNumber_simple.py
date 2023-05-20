'''
171. Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        multiple = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            k = ord(columnTitle[i]) - ord('A') + 1
            number += k * multiple
            multiple *= 26
        return number


solve = Solution()
# result = solve.titleToNumber("ABC")
result = solve.titleToNumber("AB")
print(result)
