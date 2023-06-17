def addNum(s, num):
    if s:
        cur = s.pop()
        if cur == '*':
            s.append(int(s.pop()) * int(num))
        elif cur == '/':
            s.append(int(s.pop()) / int(num))
        else:
            s.append(cur)
            s.append(num)
    else:
        s.append(num)


def dfs(chs, start, end):
    s = []
    i = start
    curNum = 0
    while i < end + 1 and chs[i] not in ')]}':
        if chs[i].isalnum():
            curNum = curNum * 10 + int(chs[i])
            if i == end or not chs[i + 1].isalnum():
                addNum(s, curNum)
                curNum = 0
        elif chs[i] in '([{':
            sub = dfs(chs, i + 1, end)
            i = sub[1]
            addNum(s, sub[0])
        else:
            s.append(chs[i])
        i += 1

    if s[0] == '-':
        res = -int(s[1])
        s = s[2:]
    else:
        res = int(s[0])
        s = s[1:]
    for j in range(0, len(s) - 1, 2):
        if s[j] == '+':
            res += int(s[j + 1])
        else:
            res -= int(s[j + 1])

    return (res, i)


# chs = '3+2*{1+2*[-4/(8-6)+7]}'
chs =input()
# chs ='(7+5*4*3+6)'
# chs = '5-3+9*6*(6-10-2)'
# chs='3*5+8-0*3-6+0+0'
# chs = '9-1+0-9+4-10-(8+4+10)-1'

lenS = len(chs)
print(dfs(chs, 0, lenS - 1)[0])
