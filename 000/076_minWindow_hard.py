'''
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。



注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成


进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0 #记录起始位置
        res = (0, float('inf'))  #用两个元素，方便之后记录起终点
        #三步骤：
        #1. 增加右边界使滑窗包含t
        for j,c in enumerate(s):
            if need[c] >0:
                needCnt -= 1
            need[c] -= 1 #这行放在外面不可以，看19行 need[c] == 0
        #2. 收缩左边界直到无法再去掉元素   !注意，处理的是i
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0: #表示再去掉就不行了(need>0)
                        break
                    else:
                        need[c] += 1
                        i += 1
                if j-i < res[1] - res[0]:  #这里是否减一都可以，只要每次都是这样算的就行，反正最后也是输出子串而非长度
                    res = (i,j)
        #3. i多增加一个位置，准备开始下一次循环(注意这步是在 needCnt == 0里面进行的 )
                need[s[i]] += 1
                needCnt += 1    #由于 移动前i这个位置 一定是所需的字母，因此NeedCnt才需要+1
                i += 1
        return "" if res[1]>len(s) else s[res[0]: res[1]+1]


solve = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
# s = "a"
# t = "a"
# s = "a"
# t = "aa"
s = "a"
t = "b"
# s = "ab"
# t = "a"
result = solve.minWindow(s, t)
print(result)
