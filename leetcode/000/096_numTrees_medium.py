'''
96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。



示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1


提示：

1 <= n <= 19
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)



solve = Solution()
n = 4
result = solve.numTrees(n)
print(result)


# class Solution:
#     def numTrees(self, n: int) -> int:
#         f = [0] * (n + 1)
#         f[0] = 1
#         f[1] = 1
#         for i in range(2, n + 1):
#             for j in range(i):
#                 f[i] += f[j] * f[i - j - 1]
#         return f[-1]