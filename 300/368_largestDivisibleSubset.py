'''
368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。



示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]


提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同
'''


class Solution:
    def largestDivisibleSubset(self, nums):
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        all = sorted(nums)
        result = [[]]
        result[0].append(all[0])
        for i in all[1:]:
            index1 = 0
            for l1 in result:
                if i % l1[0] == 0:
                    index1 = 1
                    l1.append(i)
            if index1 == 0:
                result.append([])
                result[-1].append(i)
        max = -1
        maxl = []
        for l1 in result:
            l2 = self.largestDivisibleSubset(l1[1:])
            if len(l2) > max:
                max = len(l2)
                l2.append(l1[0])
                maxl=l2
        return maxl


solve = Solution()
nums = [1, 7, 6, 8, 3, 4, 9, 2, 27, 54]
all = solve.largestDivisibleSubset(nums)
print(all)
