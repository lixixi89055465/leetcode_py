'''
692. 前K个高频单词
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。


注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。


扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。

'''


def kSort(item1, item2):
    if item1[1] > item2[1]:
        return 1
    elif item1[1] < item2[1]:
        return -1
    elif item1[0] < item2[0]:
        return 1
    elif item1[0] > item2[0]:
        return -1
    else:
        return 0


import functools
class Solution:

    def topKFrequent(self, words: list, k):
        m = {}
        for w in words:
            if w not in m.keys():
                m[w] = 0
            m[w] = m[w] + 1
        m=[i for i in m.items()]

        m_sort = sorted(m,key=functools.cmp_to_key(kSort),reverse=True)
        b = [i[0] for i in m_sort[:k]]
        return b


solve = Solution()
# la = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
la = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
result = solve.topKFrequent(la, k)
print(result)
