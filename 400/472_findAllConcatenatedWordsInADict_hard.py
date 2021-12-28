'''
472. 连接词
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。



示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]


提示：

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 105
'''


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        tRoot = self.root
        for w in word:
            if w not in tRoot:
                tRoot[w] = {}
            tRoot = tRoot[w]
        tRoot['#'] = {}

    def query(self, word):
        if len(word) == 0:
            return True
        tRoot = self.root
        for i, c in enumerate(word):
            if c in tRoot:
                tRoot = tRoot[c]
            else:
                return False
            if '#' in tRoot:
                if self.query(word[i + 1:]):
                    return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()
        words.sort(key=lambda x: len(x))
        ans = []
        for word in words:
            if not word:
                continue
            if trie.query(word):
                ans.append(word)
            else:
                trie.insert(word)
        return ans


solve = Solution()
# words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
words = ["cat", "dog", "catdog"]
result = solve.findAllConcatenatedWordsInADict(words)
print(result)
