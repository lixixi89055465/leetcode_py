'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


class Solution:
    def trap(self, height: list) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        j = 1
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
            right[-i - 1] = max(height[- i - 1], right[-i])
        result = 0
        for i in range(0, len(height)):
            result += min(left[i], right[i])-height[i]
        return result


solve = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
result = solve.trap(height)
print(result)
