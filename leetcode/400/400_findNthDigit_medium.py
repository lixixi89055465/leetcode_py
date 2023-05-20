'''
400. 第 N 位数字
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
9
90*2
900*3
9000*4
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        jiu = 9
        begin = 1
        nlen = 1
        while n > jiu * nlen:
            n -= jiu * nlen
            begin *= 10
            jiu *= 10
            nlen += 1
        # if n % nlen == 0:
        #     return 0
        tmp = begin
        if n % nlen == 0:
            tmp += n // nlen - 1
            return tmp % 10
        else:
            cur = n // nlen + begin
            for i in range(n % nlen):
                tmp = cur // begin
                cur = cur % begin
                begin //= 10
            return tmp


solve = Solution()
# n=100
'''
n=10000
output=7
'''
n = 10000
# n = 11
# n = 10
result = solve.findNthDigit(n)
print(result)
