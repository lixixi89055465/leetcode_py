'''
166. 分数到小数
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。



示例 1：

输入：numerator = 1, denominator = 2
输出："0.5"
示例 2：

输入：numerator = 2, denominator = 1
输出："2"
示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"
示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"
示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"


提示：

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''

from collections import *


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        integers = numerator // denominator
        remainer = numerator % denominator
        if not remainer:
            return str(integers)
        if numerator * denominator < 0:
            integers += 1
            remainer = denominator - remainer
        m = Counter()
        ans = ''
        while remainer and remainer not in m:
            m[remainer] += len(ans)
            remainer *= 10
            ans += str(remainer // denominator)
            remainer %= denominator

        hao = ''
        if integers == 0 and denominator * numerator < 0:
            hao = '-'

        if remainer:
            ans = hao + str(integers) + '.' + ans[:m[remainer]] + '(' + ans[m[remainer]:]
            ans += ')'
            return ans
        return hao + str(integers) + '.' + ans


solve = Solution()
# numerator = 7
# denominator = 2
numerator = 4
denominator = 333
# numerator = 1
# denominator = 2
# numerator = 2
# denominator = 1
# numerator = 2
# denominator = 3
# numerator = 1
# denominator = 5
numerator = 1
denominator = 6
# numerator = -50
# denominator = 8
# numerator = 7
# denominator = -12
result = solve.fractionToDecimal(numerator, denominator)

print(result)
