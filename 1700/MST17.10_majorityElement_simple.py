'''
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。



示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
示例 2：

输入：[3,2]
输出：-1
示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
'''


class Solution:
    def majorityElement(self, nums: list) -> int:
        m = {}
        for i in nums:
            if m.keys().__contains__(i):
                m[i] += 1
            else:
                m[i] = 1
        for i in m:
            if m[i] > len(nums) / 2:
                return i
        return -1


solve = Solution()
nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
# nums=[3,2]
# nums = [2, 2, 1, 1, 1, 2, 2]
result = solve.majorityElement(nums)
print(result)
