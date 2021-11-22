'''
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen < 2:
            return sLen
        # dp = [0 for _ in range(sLen + 1) for _ in range(sLen + 1)]
        isd = [False for _ in range(sLen + 1) for _ in range(sLen + 1)]
        for l in range(0, sLen):
            isB = True
            for i in range(0, sLen - l):
                if l == 0:
                    isd[i][i] = True
                    isB = False
                if l == 1 and s[i] == s[i + 1]:
                    isd[i][i + 1] = True
                    isB = False
                if l > 1 and isd[i + 1][i + l - 1] and s[i] == s[i + l]:
                    isd[i][i + l] = True
                    isB = False
            if isB:
                return l
        return 1


solve = Solution()
s = "babad"
result = solve.longestPalindrome(s)
print(result)
