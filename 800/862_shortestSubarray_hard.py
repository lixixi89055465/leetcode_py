'''
862. 和至少为 K 的最短子数组
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。



示例 1：

输入：nums = [1], k = 1
输出：1
示例 2：

输入：nums = [1,2], k = 4
输出：-1
示例 3：

输入：nums = [2,-1,2], k = 3
输出：3


提示：

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''

import collections


class Solution:
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        ans = N + 1
        monoq = collections.deque()
        for y, Py in enumerate(A):
            while monoq and P[monoq[-1]] >= Py:
                monoq.pop()
            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())
            monoq.append(y)
        return ans if ans < N + 1 else -1



solve = Solution()
nums = [2, -1, 2]
k = 3
# nums = [1]
# k = 1
# nums = [1, 2]
# k = 4
# nums = [48, 99, 37, 4, -31]
# k = 140
# nums = [17, 85, 93, -45, -21]
# k = 150
nums = [84, -37, 32, 40, 95]
k = 167
result = solve.shortestSubarray(nums, k)
print(result)
