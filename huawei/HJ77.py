# 该代码核心思想参考其它大神(并非自创)，我这边大概写一下我理解的思路
n, nums = input(), input().split()
res = []

def dfs(w, s, o):
    if not w and not s:
        res.append(' '.join(str(c) for c in o))
    if w:
        dfs(w[1:], w[:1] + s, o)
    if s:
        dfs(w, s[1:], o + s[:1])

dfs(nums, [], [])
# sorted 按照题目要求，字典序输出
for i in sorted(res):
    print(i)
