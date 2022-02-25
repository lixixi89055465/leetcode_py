'''
217. 存在重复元素
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。


示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例 3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true


提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        m = Counter()
        for i in nums:
            m[i] += 1
            if m[i] > 1:
                return True
        return False


solve = Solution()
nums = [1, 2, 3, 1]
result = solve.containsDuplicate(nums)
print(result)
