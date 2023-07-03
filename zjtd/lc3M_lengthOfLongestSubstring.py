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
