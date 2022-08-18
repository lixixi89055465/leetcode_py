'''
1224. 最大相等频率
给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：

从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。



示例 1：

输入：nums = [2,2,1,1,5,3,3,5]
输出：7
解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
示例 2：

输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
输出：13


提示：

2 <= nums.length <= 105
1 <= nums[i] <= 105
'''
from collections import Counter


class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and \
                    freq[maxFreq] == 1 or freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans

        # m = collections.defaultdict(int)
        # m2 = collections.defaultdict(int)
        # m[0] = len(nums)
        # ans = -1
        # for index, i in enumerate(nums):
        #     len1 = len(m2)
        #     m2[m[i]] -= 1
        #     if m2[m[i]] == 0:
        #         m2.pop(m[i])
        #         len2 = len(m2)
        #         if len2 == 2 and len1 == 3:
        #             ans = index - 1
        #     m[i] += 1
        #     m2[m[i]] += 1
        #     len2 = len(m2)
        #     if len2 == 3 and len1 == 2:
        #         ans = index
        #
        # return ans + 1


solve = Solution()
# nums = [2, 2, 1, 1, 5, 3, 3, 5]
# nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
nums = [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]
result = solve.maxEqualFreq(nums)
print(result)
