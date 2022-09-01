import collections


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        right = 0
        ans = 1
        m = collections.Counter()
        for i in s:
            if i not in m:
                right += 1
                ans = max(right - left, ans)
                m[i] += 1
                continue
            else:
                while i in m:
                    m[s[left]] -= 1
                    if m[s[left]] == 0:
                        m.pop(s[left])
                    left += 1
            m[i] += 1
            right += 1
        return ans


solve = Solution()
s="bbbbbbb"
# s="abcbdba"
# s="aabbcc"
# s = "pwwkew"
# s="a"
# s="aa"
# s=" "
# s="aaabbb"
# s = "ababababa"
# s = "abcabc"
# s = "dabcabcd"
# s = "aaaaaaaaaaaab"
# s = "aaaaabaaaaaaaa"
# s = "aaaaabbccaaaaaaaa"
# s = "abcdefghiajklmn"
# s = "aaaabbbbaaaaa"
# s = "  ab  "
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# s = "a"
# s = "abcdefghijklmnmabcdefghijklo"
# s = "abcdcabef"
result = solve.lengthOfLongestSubstring(s)
print(result)
