'''
题目链接：https://nanti.jisuanke.com/t/48

题目描述
有如下一个双人游戏：N个正整数的序列放在一个游戏平台上，两人轮流从序列的两端取数，每次有数字被一个玩家取走后，这个数字被从序列中去掉并累加到取走该数的玩家的得分中，当数取尽时，游戏结束。以最终得分多者为胜。

编一个执行最优策略的程序，最优策略就是使自己能得到在当前情况下最大的可能的总分的策略。你的程序要始终为两位玩家执行最优策略。

输入第1行包括一个正整数N（2≤N≤100）, 表示序列中正整数的个数。输入第2行包含用空格分隔的N个正整数（1≤所有正整数≤200）。

只有一行，用空格分隔的两个整数: 依次为先取数玩家和后取数玩家的最终得分。

样例输入复制

6
4 7 2 9 5 2
样例输出复制

18 11
————————————————
版权声明：本文为CSDN博主「最爱晴天和自己」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lijunyan5/article/details/83868158
'''
import string

n = int(input())
tmp = input()
arr = [int(a) for a in tmp.split()]

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
s = [0]
for i in arr:
    s.append(s[-1] + i)
for l1 in range(2, n + 1):
    for i in range(0, n - l1 + 1):
        dp[i][i + l1] = s[i + l1] - s[i] - min(dp[i + 1][i + l1], dp[i][i + l1 - 1])

print(dp)
