'''
753. 破解保险箱
有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。



示例1:

输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。


示例2:

输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。


提示：

n 的范围是 [1, 4]。
k 的范围是 [1, 10]。
k^n 最大可能为 4096。

'''

from collections import *


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join([str(i) for i in range(k)])
        # if k == 1:
        #     return '0' * n
        visited = Counter()
        result = ''

        def dfs(u):
            nonlocal result
            for i in range(k):
                tmp = u[-n + 1:] + str(i)
                if tmp not in visited:
                    visited[tmp] = 1
                    dfs(tmp)
                    result += str(i)

        dfs('0' * n)
        return result + '0' * (n - 1)


solve = Solution()
# n = 3
# k = 4
# n = 2
# k = 2
n = 1
k = 2
# n = 2
# k = 1
# n = 2
# k = 3
result = solve.crackSafe(n, k)
print(result)
