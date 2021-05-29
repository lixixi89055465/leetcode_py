'''
1190. 反转每对括号间的子串
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。



示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"


提示：

0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        left, right = 0, len(s) - 1
        la, ra = [], []
        ls = ""
        rs = ""
        ml = 0
        mr = len(s) - 1

        while left < right:
            if s[left] == '(' and s[right] == ')':
                la.append(ls)
                ls = ""
                ra.append("".join(reversed(rs)))
                rs = ""
                left += 1
                right -= 1
                ml = left
                mr = right
            if s[left] != '(':
                ls += s[left]
                left += 1
            if s[right] != ')':
                rs += s[right]
                right -= 1
        i = 0
        ls = ""
        rs = ""
        flag = 1
        while i < len(la):
            if flag > 0:
                ls += la[i]
                rs = "".join(reversed(ra[i])) + rs
                flag *= -1
            else:
                ls += "".join(reversed(ra[i]))
                rs = "".join(reversed(la[i])) + rs
                flag *= -1
            i += 1

        if flag > 0:
            result = ls + s[ml: mr + 1] + rs
        else:
            result = ls + "".join(reversed(s[ml: mr + 1])) + rs

        return result


solve = Solution()
# "apmnolkjihgfedcbq
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
# s = "(u(love)i)"
# s = "yfgnxf"
s = "ta()usw((((a))))"
result = solve.reverseParentheses(s)
print(result)
