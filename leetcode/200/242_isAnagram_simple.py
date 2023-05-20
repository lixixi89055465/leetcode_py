'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
'''

from collections import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sm = Counter()
        tm = Counter()
        for i, j in zip(s, t):
            sm[i] += 1
            tm[j] += 1
        if sm == tm:
            return True
        return False


solve = Solution()
# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
s = 'a'
t = 'ab'
result = solve.isAnagram(s, t)
print(result)
