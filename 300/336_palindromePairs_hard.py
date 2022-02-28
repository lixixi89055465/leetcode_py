'''
336. 回文对
给定一组 互不相同 的单词， 找出所有 不同 的索引对 (i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。



示例 1：

输入：words = ["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：words = ["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
示例 3：

输入：words = ["a",""]
输出：[[0,1],[1,0]]

提示：

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] 由小写英文字母组成
'''
from collections import *


class Solution:
    def palindromePairs(self, words):
        pos = defaultdict()
        for i, v in enumerate(words):
            pos[v] = i
        print(pos)
        ans = []
        for i, v in enumerate(pos):
            w = ''.join(reversed(v))
            if w in pos and i!=pos[w]:
                ans.append([i,pos[w]])
        return ans



solve = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
result = solve.palindromePairs(words)
print(result)
