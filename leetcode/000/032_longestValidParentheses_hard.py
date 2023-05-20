'''
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        maxL = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
                if right == left:
                    maxL = max(maxL, 2 * left)
                elif right > left:
                    left, right = 0, 0
        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
                if left == right:
                    maxL = max(maxL, 2 * right)
                elif left > right:
                    left, right = 0, 0
            elif s[i] == ')':
                right += 1
        return maxL


solve = Solution()
s = ")()())"
# s = "(()"
# s = ""
s = "()"
result = solve.longestValidParentheses(s)
print(result)
