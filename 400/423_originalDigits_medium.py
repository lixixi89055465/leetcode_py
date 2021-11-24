'''
423. 从英文中重建数字
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。



示例 1：

输入：s = "owoztneoer"
输出："012"
示例 2：

输入：s = "fviefuro"
输出："45"


提示：

1 <= s.length <= 105
s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
s 保证是一个符合题目要求的字符串
'''


class Solution:
    def originalDigits(self, s: str) -> str:
        n0 = s.count('z')
        n2 = s.count('w')
        n4 = s.count('u')
        n6 = s.count('x')
        n8 = s.count('g')
        n3 = s.count('h') - n8
        n5 = s.count('f') - n4
        n7 = s.count('v') - n5
        n1 = s.count('o') - n0 - n2 - n4
        n9 = s.count('i') - n5 - n6 - n8
        ns = (n0, n1, n2, n3, n4, n5, n6, n7, n8, n9)
        return "".join(str(i) * n for i, n in enumerate(ns))


solve = Solution()
s = "owoztneoer"
result = solve.originalDigits(s)
print(result)
