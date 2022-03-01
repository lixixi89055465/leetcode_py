'''
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。


'''

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, h):
        m = Counter()
        for i in nums:
            m[i] += 1
        ans = []
        for k in m:
            heapq.heappush(ans, (-m[k], k))
        return [heapq.heappop(ans)[1] for i in range(h)]


solve = Solution()
# nums = [1, 3, 1, 2, 0, 5]
# k = 3
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = solve.topKFrequent(nums, k)
print(result)
