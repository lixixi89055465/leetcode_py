'''
1154. 一年中的第几天
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。



示例 1：

输入：date = "2019-01-09"
输出：9
示例 2：

输入：date = "2019-02-10"
输出：41
示例 3：

输入：date = "2003-03-01"
输出：60
示例 4：

输入：date = "2004-03-01"
输出：61


提示：

date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        a = date.split('-')
        year = int(a[0])
        month = int(a[1])
        days = int(a[2])

        def getMonthDay(rui, m):
            s = 0
            for i in range(1, m):
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                    s += 31
                elif i == 2:
                    if rui:
                        s += 29
                    else:
                        s += 28
                else:
                    s += 30
            return s

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return getMonthDay(1, month) + days
        else:
            return getMonthDay(0, month) + days


solve = Solution()
date = "2003-03-01"
date = "2100-03-01"
result = solve.dayOfYear(date)
print(result)
