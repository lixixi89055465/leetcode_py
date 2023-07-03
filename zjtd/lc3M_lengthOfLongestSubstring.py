'''
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        chs = [-1 for _ in range(128)]
        ans = 0
        curan = 0
        lastPre = -1
        for i in range(len(s)):
            if chs[ord(s[i])] >= 0:
                lastPre=max(chs[ord(s[i])],lastPre)
                ans = max(ans, i - lastPre)
                curan = i - lastPre
                chs[ord(s[i])] = i
            else:
                chs[ord(s[i])] = i
                curan += 1
                ans = max(ans, curan)
        return ans


solve = Solution()
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "aab"
s = "abba"

res = solve.lengthOfLongestSubstring(s)
print(res)
