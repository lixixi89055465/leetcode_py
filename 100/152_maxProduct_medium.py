'''
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
通过次数203,596提交次数482,208
'''


class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        fmi = nums[0]
        fma = nums[0]
        ans = nums[0]

        for i in range(1,n):
            mi, ma = fmi, fma
            fmi = min(mi * nums[i], ma * nums[i], nums[i])
            fma = max(mi * nums[i], ma * nums[i], nums[i])
            ans = max(fma, ans)
        return ans


solve = Solution()
nums = [2, 3, -2, 4]
nums = [-2]
result = solve.maxProduct(nums)
print(result)
