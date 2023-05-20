'''
229. 求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。





示例 1：

输入：[3,2,3]
输出：[3]
示例 2：

输入：nums = [1]
输出：[1]
示例 3：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]


提示：

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109


进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
'''

from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        x = float('-inf')
        xn = 0
        y = float('-inf')
        yn = 0
        for i in nums:
            if i == x or xn == 0:
                x = i
                xn += 1
            elif i == y or yn == 0:
                y = i
                yn += 1
            else:
                xn -= 1
                yn -= 1
        ans=[]
        if yn>0:
            ans.append(y)
        if xn>0:
            ans.append(x)
        return ans


solve = Solution()
nums = [1, 1, 1, 3, 3, 2, 2, 2]
nums=[3,2,3]
result = solve.majorityElement(nums)
print(result)
