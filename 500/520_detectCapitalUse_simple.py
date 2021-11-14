'''
520. 检测大写字母
我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如 "USA" 。
单词中所有字母都不是大写，比如 "leetcode" 。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。



示例 1：

输入：word = "USA"
输出：true
示例 2：

输入：word = "FlaG"
输出：false
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 0:
            return False
        if len(word) == 1:
            return True
        if word[0] <= 'z' and word[0] >= 'a':
            for c in word[1:]:
                if c > 'z' or c < 'a':
                    return False
            return True
        elif word[0] >= 'A' and word[0] <= 'Z':
            if word[1] >= 'A' and word[1] <= 'Z':
                for c in word[2:]:
                    if c < 'A' or c > 'Z':
                        return False
                return True
            else:
                for c in word[2:]:
                    if c > 'z' or c < 'a':
                        return False
                return True

        return True


solve = Solution()
# word = "USA"
# word = "FlaG"
# word="ffffffffffffffffffffF"
word = "aeafawA"
result = solve.detectCapitalUse(word)
print(result)
