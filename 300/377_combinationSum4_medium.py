'''
377. 组合总和 Ⅳ
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。



示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
'''


class Solution:
    def __init__(self):
        self.count = 0

    def combine(self, nums, target):
        for i in nums:
            if i < target:
                self.combine(nums, target - i)
            elif i == target:
                self.count += 1
                return
            else:
                return

    def combinationSum4(self, nums, target):
        nums = sorted(nums)
        self.combine(nums, target)
        return self.count


solve = Solution()
nums = [1, 2, 3]
target = 4
nums = [3, 1, 4, 2]
target = 4
nums = [4, 2, 1]
target = 32
result = solve.combinationSum4(nums, target)
print(result)
