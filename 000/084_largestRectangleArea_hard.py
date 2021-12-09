'''
largestRectangleArea
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。



示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4


提示：

1 <= heights.length <=105
0 <= heights[i] <= 104
'''

#
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        s = []
        i = 0
        n = len(heights)
        left, right = [0] * n, [n] * n
        print(heights)
        while i < n:
            while s and heights[s[-1]] > heights[i]:
                right[s[-1]] = i
                s.pop()
            left[i] = s[-1] if s else -1
            s.append(i)
            i += 1
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

# class Solution:
#     def largestRectangleArea(self, heights: list) -> int:
#         n = len(heights)
#         left, right = [0] * n, [n] * n
#
#         mono_stack = list()
#         for i in range(n):
#             while mono_stack and heights[mono_stack[-1]] >= heights[i]:
#                 right[mono_stack[-1]] = i
#                 mono_stack.pop()
#             left[i] = mono_stack[-1] if mono_stack else -1
#             mono_stack.append(i)
#
#         ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
#         return ans


solve = Solution()
# heights = [2, 1, 5, 6, 2, 3]
heights = [2,4]
heights = [3,1,3,2,2]

result = solve.largestRectangleArea(heights)
print(result)
