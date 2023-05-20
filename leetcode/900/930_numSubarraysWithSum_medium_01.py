'''
930. 和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。



示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15


提示：

1 <= nums.length <= 3 * 104
nums[i] 不是 0 就是 1
0 <= goal <= nums.length
'''


class Solution:
    def numSubarraysWithSum(self, nums: list, goal: int) -> int:
        s = 0
        sA = []
        m = {}
        result = 0
        m[0] = 1
        for i in nums:
            s += i
            if m.keys().__contains__(s):
                m[s] += 1
            else:
                m[s] = 1
            sA.append(s)
            # if m.keys().__contains__(i - goal):
            #     result += m[s - goal]
        print(sA)
        print(m)
        for i in sA:
            if i >= goal and m.keys().__contains__(i - goal):
                result += m[i - goal]
        return result


solve = Solution()
nums = [1, 0, 1, 0, 1,1,1]
goal = 2
# nums = [0, 0, 0, 0, 0]
# goal = 0
result = solve.numSubarraysWithSum(nums, goal)
print(result)
