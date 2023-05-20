'''
159. 至多包含两个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。
'''

from collections import *


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = Counter()
        left = 0
        ans = 0
        for i, ch in enumerate(s):
            m[ch] += 1
            right = i
            while len(m) > 2:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    m.pop(s[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans


solve = Solution()
# s = "eceba"
s = "ccaabbb"
result = solve.lengthOfLongestSubstringTwoDistinct(s)
print(result)
