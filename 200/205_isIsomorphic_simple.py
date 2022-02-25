'''
205. 同构字符串
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true


提示：

1 <= s.length <= 5 * 104
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成
'''

from collections import *


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m1 = defaultdict()
        m2 = defaultdict()
        for i in range(n):
            if s[i] in m1:
                if m1[s[i]] != t[i] or m2[t[i]] != s[i]:
                    return False
            elif t[i] in m2:
                if m2[t[i]] != s[i] or m1[s[i]] != t[i]:
                    return False
            else:
                m1[s[i]] = t[i]
                m2[t[i]] = s[i]
        return True


solve = Solution()
s = "egg"
t = "add"
# s = "foo"
# t = "bar"
# s = "badc"
# t = "baba"
result = solve.isIsomorphic(s, t)
print(result)
