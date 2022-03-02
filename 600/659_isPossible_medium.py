'''
659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。

如果可以完成上述分割，则返回 true ；否则，返回 false 。



示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
示例 3：

输入: [1,2,3,4,4,5]
输出: False


提示：

1 <= nums.length <= 10000
'''

from collections import defaultdict
import heapq


class Solution:
    def isPossible(self, nums):
        m = defaultdict(list)
        for i in nums:
            if i - 1 not in m:
                heapq.heappush(m[i], 1)
            else:
                a = heapq.heappop(m[i - 1])
                if len(m[i - 1]) == 0:
                    m.pop(i - 1)
                heapq.heappush(m[i], a + 1)
        for k in m:
            if min(m[k]) < 3:
                return False
        return True


solve = Solution()
nums = [1, 2, 3, 3, 4, 4, 5, 5]
result = solve.isPossible(nums)
print(result)
