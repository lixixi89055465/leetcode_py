'''
525. 连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。



示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。


提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
'''


class Solution:
    def findMaxLength(self, nums: list) -> int:
        A = 0
        Amap = {}
        maxl = 0
        Amap[0] = -1
        for i, e in enumerate(nums):
            if e:
                A += 1
            else:
                A -= 1
            if Amap.__contains__(A):
                maxl = max(i - Amap[A], maxl)
            else:
                Amap[A] = i
        return maxl


solve = Solution()
nums = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
result = solve.findMaxLength(nums)
print(result)
