'''
632. 最小区间
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。



示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释：
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]


提示：

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] 按非递减顺序排列
'''

import heapq


class Solution:
    def smallestRange(self, nums):
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        smallE = [(v[0], i, 0) for i, v in enumerate(nums)]
        maxValue = max([e[0] for e in smallE])
        heapq.heapify(smallE)
        while True:
            minValue, row, idx = heapq.heappop(smallE)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(smallE, (nums[row][idx + 1], row, idx + 1))
        return [rangeLeft, rangeRight]


solve = Solution()
nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
result = solve.smallestRange(nums)
print(result)
