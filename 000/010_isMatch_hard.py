'''
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


示例 1：

输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：

输入：s = "mississippi" p = "mis*is*p*."
输出：false


提示：

1 <= s.length <= 20
1 <= p.length <= 30
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        parr = []
        i = 0
        while i < len(p):
            if i != len(p) - 1:
                if p[i].isalpha():
                    if p[i + 1] == '*':
                        parr.append(p[i: i + 2])
                        i += 2
                        continue
                    if p[i + 1] == '.':
                        parr.append(p[i])
                        parr.append(p[i + 1])
                        i += 2
                        continue
                    if p[i + 1].isalpha():
                        parr.append(p[i])
                        i += 1
                        continue
                elif p[i] == '.':
                    if p[i + 1] == '*':
                        parr.append(p[i:i + 2])
                        i += 2
                    else:
                        parr.append(p[i])
                        i += 1


            else:
                parr.append(p[-1])
                i += 1
        j = 0
        for i in parr:
            if len(i) == 1:
                if i == '.':
                    j += 1
                    continue
                else:
                    if j >= len(s):
                        return False
                    if i[0] != s[j]:
                        return False
                    j += 1
                    continue
            if len(i) == 2:
                if i[0] == '.':
                    if len(parr) == 1:
                        return True
                    else:
                        break
                if i[1] == '*':
                    if j >= len(s):
                        return False
                    if i[0] == s[j]:
                        while i[0] == s[j]:
                            j += 1
                            if j >= len(s):
                                break
        return j == len(s)


solve = Solution()
# s = "aab"
# p = "c*a*b"
# s = "mississippi"
# p = "mis*is*p*."
# s = "ab"
# p = ".*"
# s = "aa"
# p = "a*"
# s = "aa"
# p = "a"
# s = "ab"
# p = ".*c"
# s = "aaa"
# p = "aaaa"
s="aaa"
p="a*a"
result = solve.isMatch(s, p)
print(result)
