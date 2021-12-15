'''
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典，判定 s 是否可以由空格拆分为一个或多个在字典中出现的单词。

说明：拆分时可以重复使用字典中的单词。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false


提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅有小写英文字母组成
wordDict 中的所有字符串 互不相同
'''


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        def isP(s):
            for i in wordDict:
                if s == i:
                    return True
            return False

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(max(0, i - 20), i):
                if dp[j] and isP(s[j:i]):
                    dp[i] = True
                    break
        # print(dp)
        return dp[-1]


solve = Solution()
# s = "applepenapple"
# wordDict = ["apple", "pen"]
# s = "leetcode"
# wordDict = ["leet", "code"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
result = solve.wordBreak(s, wordDict)
print(result)
