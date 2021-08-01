'''
面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
通过次数14,411提交次数20,785
'''


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        m = {}
        for s in strs:
            k = "".join(sorted(s))
            if m.keys().__contains__(k):
                m[k].append(s)
            else:
                m[k] = [s]
        result = []
        for i in m:
            result.append(m[i])
        return result


solve = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solve.groupAnagrams(strs)
print(result)
