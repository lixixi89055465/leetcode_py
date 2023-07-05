'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

'''


class Solution(object):
    def trap(self, height):
        hlen = len(height)
        stack = list()
        ans = 0
        left, right = 0, hlen - 1
        leftMax = height[0]
        rightMax = height[hlen - 1]
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solve = Solution()
print(solve.trap(height))
