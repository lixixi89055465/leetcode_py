'''
312. 戳气球
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。



示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
示例 2：

输入：nums = [1,5]
输出：10


提示：

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
'''


class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return nums[0] * nums[1] + max(nums) ** 2
        dp = [0] * (n + 1)

        def dfs(arr, extra):
            na = len(arr)
            if na == 1:
                return nums[0] * extra + max(nums[0], extra) ** 2
            else:
                return max(dp[na - 1] + arr[n - 1] * extra, dfs(arr[:-1] + arr[-2] * arr[-1] * arr))

        for i in range(n):
            dp[i] = max(dp[i - 1] + nums[i - 1] * nums[i],
                        dfs(nums[:i - 1], nums[i]) + nums[i - 2] * nums[i - 1] * nums[i])


solve = Solution()
nums = [3, 1, 5, 8]
result = solve.maxCoins(nums)
print(result)
