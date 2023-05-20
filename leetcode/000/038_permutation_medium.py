'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


限制：

1 <= s 的长度 <= 8
a : a
ab : ab,ba
abc : cab,acb,abc, cba,bca,bac
abcd: dcab,cdab,cadb,cabd,
      dacb,adcb,acdb,acbd,

'''


class Solution:
    def permutation(self, s: str) -> list:
        result = set([])
        result.add(s[0])
        for c in s[1:]:
            resultTmp = set([])
            for l in result:
                # resultTmp += [list(l).insert(i, c) for i in range(len(l) + 1)]
                for i in range(len(l) + 1):
                    t = list(l)
                    t.insert(i, c)
                    resultTmp.add(''.join(t))
            result = resultTmp
        return list(result)


solve = Solution()
result = solve.permutation("abc")
print(result)
