'''
318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。



示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
'''
from functools import reduce
from itertools import product


class Solution:
    def maxProduct(self, words) -> int:
        mask = [reduce(lambda a, b: a | b, [1 << (ord(c) - ord('a')) for c in v]) for v in words]
        return max(
            (len(x[1]) * len(y[1]) for x, y in product(zip(mask, words), repeat=2) if x[0] & y[0] == 0), default=0)


solve = Solution()
# word = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# word=["a","ab","abc","d","cd","bcd","abcd"]
word=["a","aa","aaa","aaaa"]
result = solve.maxProduct(word)
print(result)
