'''
629. K个逆序对数组
给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

示例 1:

输入: n = 3, k = 0
输出: 1
解释:
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2:

输入: n = 3, k = 1
输出: 2
解释:
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
'''


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n + 1)]
        for i in range(1,n):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                if i*(i-1)<j*2:
                    break
                if j > i:
                    for t in range(1, i + 1):
                        dp[i][j] += dp[i - 1][j - t + 1]
                else:
                    for t in range(1, j + 1):
                        dp[i][j] += dp[i - 1][j - t + 1]
        for i in range(n+1):
            print(dp[i])
        return dp[n][k]


solve = Solution()
n = 4
k = 2
result = solve.kInversePairs(n, k)
print(result)
