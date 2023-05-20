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
        n = len(s)
        pair = [0 for _ in range(len(s))]
        stk = []
        for i in range(0, n):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                j = stk.pop()
                pair[i], pair[j] = j, i
        ret = ""
        index = 0
        step = 1
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = pair[index]
                step = -step
            else:
                ret += s[index]
            index += step
        return ret


solve = Solution()
# "apmnolkjihgfedcbq
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
# s = "(u(love)i)"
# s = "yfgnxf"
s = "ta()usw((((a))))"
result = solve.reverseParentheses(s)
print(result)
