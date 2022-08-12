'''
牛妹给了牛牛一个长度为  的下标从开始的正整型数组  ，粗心的牛牛不小心把其中的一些数字删除了。

假如被删除了，则。对于所有被删除的数字，牛牛必须选择一个正整数填充上。现在牛牛想知道有多少种填充方案使得：

 且对于所有的满足 。
函数传入一个下标从开始的数组  和一个正整数  ，请返回合法的填充方案数对 取模的值,保证不存在方案数为0的数据。
'''


class Solution:
    def FillArray(self, a, k):
        fillArr = list()
        start = -1
        flag = 0  # 0表示上一个是正数，1表示上一个是0
        a = [1] + a + [k]
        for i, v in enumerate(a):
            if v > 0 and flag == 0:
                start = i
                flag = 0
            elif v > 0 and flag == 1:
                fillArr.append((min(v, k) - a[start], i - start - 1))
                flag = 0
                start = i
            elif v == 0 and flag == 0:
                flag = 1
            elif v == 0 and flag == 1:
                continue

        def findDp(n, m):
            dp = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(1, m + 1):
                dp[0][i] = 1
            for j in range(1, n + 1):
                dp[j][0] = 1
            cheng = 10 ** 9 + 7
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % cheng
            return dp

        maxN, maxM = 0, 0
        for i, j in fillArr:
            maxN = max(maxN, i)
            maxM = max(maxM, j)
        dp = findDp(maxN, maxM)
        result = 1
        cheng = 10 ** 9 + 7

        for i, j in fillArr:
            result = (result * dp[i][j]) % cheng
        return result

        # for i, j in fillArr:


a = [0, 4, 5]
k = 6
a = [1, 0, 0]
k = 3
a = [0, 0, 0, 0, 0, 67, 0, 0]
k = 100
a = [1, 0, 0, 3, 0]
k = 100
solve = Solution()
result = solve.FillArray(a, k)
print(result)
