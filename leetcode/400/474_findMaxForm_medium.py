'''
474. 一和零
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。



示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
'''


class Solution:
    def findMaxForm(self, strs, m, n) -> int:
        l = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l + 1)]
        for i in range(len(strs)):
            zeros, ones = self.getOneTwo(strs[i])
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    dp[i + 1][j][k] = dp[i][j][k]
                    if j >=zeros and k >= ones:
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - zeros][k - ones] + 1)
        return dp[l][m][n]

    def getOneTwo(self, str1):
        nums = [0, 0]
        for c in str1:
            if c == '0':
                nums[0] += 1
            else:
                nums[1] += 1
        return nums


solve = Solution()
# strs = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3


strs=["10","0","1"]
m=1
n=1


result = solve.findMaxForm(strs, m, n)
print(result)
