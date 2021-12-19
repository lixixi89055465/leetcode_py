'''
233. 数字 1 的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。



示例 1：

输入：n = 13
输出：6
示例 2：

输入：n = 0
输出：0


提示：

0 <= n <= 109
通过次数36,300提交次数76,093
'''


class Solution:
    def countDigitOne(self, n: int) -> int:
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans


solve = Solution()
# n = 10000
n = 13
result = solve.countDigitOne(n)
print(result)
